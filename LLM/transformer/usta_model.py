import torch
import torch.nn as nn

from usta_multi_head_attention import UstaMultiHeadAttention


def get_rotary_position_encoding(input: torch.Tensor, base=10000, device="cpu"):
  # input: Şeklî (uzunluk, genişlik) olan bir tablo gibi düşün.
  # uzunluk = kaç tane oyuncak var (kaç pozisyon)
  # genişlik = her oyuncağın kaç rengi/özelliği var (boyut)
  context_length, dimension = input.shape

  # Genişlik çift olmalı; çünkü yarısını sağ grup, yarısını sol grup yapacağız
  assert dimension % 2 == 0, "dimension must be even"

  # Genişliğin yarısı (sağ ve sol gruplar için)
  half_dimension = dimension // 2

  # freqs_indices: 0'dan yarıya kadar sayılar (farklı “hızlarda” döndürmek için)
  freqs_indices = torch.arange(0, half_dimension, device=device, dtype=torch.float32)

  # freqs: Her özellik için farklı bir “dönme hızı” (büyüdükçe daha yavaş)
  # base büyük bir sayı; üstler bölündükçe küçük değerler çıkar, frekans gibi davranır
  freqs = 1.0 / (base ** (freqs_indices / dimension))

  # positions: 0, 1, 2, ... gibi sırayla oyuncakların konum numaraları (dike diziyoruz)
  positions = torch.arange(0, context_length, device=device, dtype=torch.float32).unsqueeze(1)

  # angles: Her konum için (pozisyon) ve her hız için (freq) çarpıp bir “açı” elde ediyoruz
  angles = positions * freqs

  # Bu açının sinüs ve kosinüs değerleri: dönme işleminin sihirli tuzu
  sin_angles = torch.sin(angles)
  cos_angles = torch.cos(angles)

  # input'un yarısını “çiftler” (ilk yarı), diğer yarısını “tekler” (ikinci yarı) gibi ayır
  # (Sanki kart destesini ikiye bölmek gibi)
  input_even = input[:, :dimension // 2]  # ilk yarı
  input_odd  = input[:, dimension // 2:]  # ikinci yarı

  # DÖNDÜRME SİHİRİ:
  # x' = x * cos - y * sin
  # y' = x * sin + y * cos
  # Böylece iki yarıyı birbirine göre nazikçe döndürmüş oluyoruz
  input_even_rotated = input_even * cos_angles - input_odd * sin_angles
  input_odd_rotated  = input_even * sin_angles + input_odd * cos_angles
  
  # Aynı boyutta boş bir kutu hazırlıyoruz, içine döndürülmüş halleri koyacağız
  input_rotated = torch.empty_like(input)

  # İlk yarıya döndürülmüş “çiftler”, ikinci yarıya döndürülmüş “tekler” gider
  input_rotated[:, :dimension // 2] = input_even_rotated
  input_rotated[:, dimension // 2:] = input_odd_rotated

  # Ve döndürülmüş renkli oyuncaklarımızı geri veriyoruz :)
  return input_rotated



class UstaModel(nn.Module):
  def __init__(self, vocab_size, embedding_dim, num_heads, context_length ):
    super().__init__()

    self.embedding = nn.Embedding(vocab_size, embedding_dim)
    #Dont use it only example
    self.pos_embedding = nn.Embedding(vocab_size, embedding_dim)
    self.get_pos = get_rotary_position_encoding
    self.self_attation = UstaMultiHeadAttention(embedding_dim, embedding_dim, context_length, num_heads, dropout_rate=0.5)

  def forward(self, x: torch.Tensor):
    x = self.embedding(x) # dictionary meaning of the tokens (words)
    x = self.self_attation(x) 
    return x