import ftplib

ftp = ftplib.FTP("test.rebex.net")
logowanie = ftp.login("demo", "password")
print(logowanie)
katolog = ftp.nlst()
print(katolog)
plik = ftp.retrbinary("RETR readme.txt", open ("plik_z_ftp.txt", "wb").write)
print(plik)

katolog2 = ftp.nlst("pub/example")
print(katolog2)
plik2 = ftp.retrbinary("RETR pub/example/KeyGenerator.png", open("grafika.png", "wb").write)