def main():
    while True:
        print("\nGelişmiş Müzik Çalar Uygulaması")
        print("1. Müzik çal")
        print("2. Müzik durdur")
        print("3. Müzik duraklat/Devam ettir")
        print("4. Ses seviyesini ayarla")
        print("5. Sonraki şarkı")
        print("6. Önceki şarkı")
        print("7. Çıkış")

        choice = input("Seçiminizi yapın (1/2/3/4/5/6/7): ")

        if choice == '1':
            file = input("Müzik dosyasının yolunu girin: ")
            play_music(file)
        elif choice == '2':
            stop_music()
        elif choice == '3':
            if paused:
                unpause_music()
                paused = False
            else:
                pause_music()
                paused = True
        elif choice == '4':
            volume = float(input("Ses seviyesini girin (0.0 - 1.0): "))
            set_volume(volume)
        elif choice == '5':
            current_track = (current_track + 1) % len(music_files)
            play_music(music_files[current_track])
        elif choice == '6':
            current_track = (current_track - 1) % len(music_files)
            play_music(music_files[current_track])
        elif choice == '7':
            stop_music()
            pygame.quit()
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")
