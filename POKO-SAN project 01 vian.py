

#welcome_message = '''  ^^   WELCOME TO     *****
#****     POKOMOKO GAMES ! '''

#print('''********************************''')
#print(f'''**** {welcome_message} *****''')
#print('''********************************''')

welcome_message = '''  ^^ WELCOME TO ⋆⁺₊✧. =====
======   POKOMOKO GAMES ! '''

print('''
================================''')
print(f'''====={welcome_message}====== 
======  ⎛⎝ ≽ > ⩊ < ≼ ⎠⎞  =======''')
print('''================================''')

import random

Pokosan_position_level_1 = random.randint(1,2)
Pokosan_position_level_2 = random.randint(1,3)
Pokosan_position_level_3 = random.randint(1,4)

user = input('''       
˚ ⋅ᯓ★ Masukan nama anda˚ ⋅ᯓ★ :
             ''')

print(f'''
Hi {user} !,
Pilih Poko-san mu disinii ! ^-^
   
૮(> ⤙ <)ა     "૮₍˶•⤙•˶₎ა 
    1              2
    
 ≽^•˕•^≼       ᓚ₍⑅^..^₎♡
    3               4     
''')
type_1 = '૮(> ⤙ <)ა'
type_2 = '"૮₍˶•⤙•˶₎ა'
type_3 = '≽^•˕•^≼'
type_4 = 'ᓚ₍⑅^..^₎♡'

Choose = input(''' 
Pilih :
type_1
type_2
type_3
type_4

di bawah sini
= 
 ''')

print(f'''Haloo {user} !, Kamu akan bermain dengan {Choose} !''')

if Choose == 'type_1' :
    print('૮(> ⤙ <)ა')
    
elif Choose == 'type_2' :
    print('"૮₍˶•⤙•˶₎ა')
    
elif Choose == 'type_3' :
    print('≽^•˕•^≼')
    
else:
    print('ᓚ₍⑅^..^₎♡')
    
print(f'''{user} !, 
      Coba Perhatikan Goa-Goa di bawah ini! ⋆⁺₊✧ 
      [_]       [_]
     Goa 1     Goa 2 ''')

print(f'''Menurut {user} di Goa Nomor Berapa Poko-san Berada? ₍^.c.^₎⟆''')
nomor_goa_level_1 = [1],[2]
print (nomor_goa_level_1)

a=int(input('''Poko-san ada di goa
           nomor = '''))

print(f'''Pilihan {user} adalah {a}, 
          Apakah {user} yakin jawabannya ada di nomor {a}? ₍ᐢ.v.ᐢ₎''')

confirm_1=input(''' Yes / No 
                  = ''')

if int (a) == Pokosan_position_level_1 :
    print(f'''Selamat {user} !⋅ᯓ★
             Jawaban kamu benarr 
             ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧
             
             Posisi Poko-san ada di goa nomor itu,
             Kamu bisa lanjut ke level 2 deh 
             ᓚ₍⑅^..^₎♡
             
             ''')
else:
    print(f'''YAHH SALAHH!( ꩜ ᯅ ꩜;)
          Poko-san bukan berada di goa yg ituu ₍^._.^₎⟆
          Tapi ada di goa nomor {Pokosan_position_level_1} !''')
    
b =input('''Lanjut ke level 2 ?
            ⸜(｡˃ ᵕ < )⸝♡

           [yes] / [No] 
           =''')

if (b) == 'yes':
 print(f'''Sekarang bakal lebih susah lagi nih! ≽^•˕•^≼
          Menurut {user} di Goa Nomor Berapa Poko-san Berada?''')
else:
    print(f'''Mungkin {user} dapat mengulang level 1 dulu.... ૮(˶ᵔ v ᵔ˶)ა''')
    
nomor_goa_level_2 = [1],[2],[3]
print(nomor_goa_level_2)

c =int(input('''Poko-san ada di goa
           nomor = '''))

print(f'''Pilihan {user} adalah {c}, 
          Apakah {user} yakin jawabannya ada di nomor {c}? ₍⑅ᐢ..ᐢ₎''')

confirm_2=input(''' Yes / No 
                  = ''')

if int (c) == Pokosan_position_level_2 :
    print(f'''Selamat {user}!⋅ᯓ★
             Jawaban kamu benarr 
             ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧
              
             Posisi Poko-san ada di goa nomor itu,
             Kamu bisa lanjut ke level 3 deh! 
             ≽^•⩊•^≼ ᯓ ᡣ𐭩
             ''')
else:
    print(f'''YAHH SALAHH! ( ꩜ ᯅ ꩜;)
          Poko-san bukan berada di goa yg ituu :(
          Tapi ada di goa nomor {Pokosan_position_level_2} ₍ᐢ._.ᐢ₎ !''')
    
    
d =input('''Lanjut ke level 3 ? ૮(> ⤙ <)ა
           [yes] / [No] 
           =''')

if (d) == 'yes':
 print(f'''Sekarang bakal lebih susah lagi nih! (˶°ㅁ°) !!
          Menurut {user} di Goa Nomor Berapa Poko-san Berada?''')
else:
    print(f'''Mungkin {user} dapat mengulang level 2 dulu ૮(˶ᵔᵕᵔ˶)ა .... ''')
    
nomor_goa_level_3 = ('''
                     [1]     [2]
                       [3]      [4]
                       ''')
print(nomor_goa_level_3)

cheat = Pokosan_position_level_3
print(cheat)

e =int(input('''Poko-san ada di goa
           nomor = '''))

print(f'''Pilihan {user} adalah {e}, 
          Apakah {user} yakin jawabannya ada di nomor {e}?''')

confirm_3=input(''' Yes / No 
                  = ''')

if int (e) == Pokosan_position_level_3 :
    print(f'''
             ⋅ᯓ★ JAWABAN KAMU BENAR ^_^ 🎉 !
             Posisi Poko-san ada di goa nomor itu,
             SELAMAT, KAMU SUDAH BERHASIL MENEBAK SEMUA POSISI POKO-SAN SAMPAI AKHIR ! ₊˚⊹ ᰔ
             
             ⋅˚₊‧ 🜲 ‧₊˚ 
            KAMU MENANG {user}!
             
             {user} berhak mendapatkan piala! 
             ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧🏆ᯓ★
             
             
                 
            ==== ≽^• ˕ •^≼ ===
            ⋅ᯓ★ GAME OVER ⋅ᯓ★
            ✩₊˚ ========== ✩₊˚
            
            
            ⋆.˚✮ 𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦 ✮˚.⋆
                for playing
                 
                    𓆩♡𓆪
                     
                     
            Created by : Revian
            
                  
            ⎛⎝ ≽ > ⩊ < ≼ ⎠⎞   
            
               Hak Cipta ©          
               ────୨ৎ────
''')
else:
    print(f'''YAHH SALAHH! ( ꩜ ᯅ ꩜;)
          
          Poko-san bukan berada di goa yg ituu :(
          Tapi ada di goa nomor {Pokosan_position_level_3} ₍ᐢ._.ᐢ₎ !
          level ini memang sulit si...
          "૮(˶•⤙•˶)ა
          
          Coba lagi yu, jangan menyerahhh! ₊˚ ⋅ᯓ★ 
          
                 
          ⎛⎝ ≽ > ⩊ < ≼ ⎠⎞  ₊˚⊹ ᰔ
               
            ₊──── ୨୧ ────⋆ 
            
          ''')


