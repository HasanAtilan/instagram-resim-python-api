#!/usr/bin/env python
#
#
# HasanAtilan.Com

from InstaVeri import InstaVeri

InstaVeri = InstaVeri("kullanici", "sifre")
InstaVeri.giris()  # giris

resimklasor = '/resim/resim.png'
aciklama = "Test Resim"
InstaVeri.uploadPhoto(resimklasor, aciklama=aciklama)
