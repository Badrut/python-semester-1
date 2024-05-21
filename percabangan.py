# mengkategorikan layak tidaknya seseorang dalam mengnonton film
# imdikatornya adalah usia 
# jika usianya lebih dari 17 tahun maka layak
# jika tidak maka belum layak

keinginan = int(input("apakah kamu mau denganku ="))

if( keinginan > 10):
    print("layak untuk bersamanya")
else:
    print("maaf anda belum layak untuk memilikinya")

#kategorikan kelulusan dari nilai
#indikatornya adalah nilai
#syarat:
#lulus jika nilai > 90
#pushup dulu baru lulus jika nilai > 70
#tidak lulus jika nilai < 70

lulus = int(input(" berapa nilaimu ="))
if(lulus > 90):
    print("selamat anda lulus")
elif(lulus > 70):
    print("pushup sek lagi lulus")
else:
    print("maaf anda tidak lulus")

