# Projekt 2
## Projekt: "Wtyczka do QGIS - PyQGIS"
### Jak działa i do czego służy?
--------------------
Głównym celem projektu jest stworzenie wytczki kompatyblinej z opragromowaniem QGIS. Wtyczka pozwoli użytkownikowi użyć kilku przydatnych funkcjonalności w programie QGIS. Poniżej znajduje się lista możliwości jakie posiada aplikacja?:  

- Obliczenie różnicy wysokości pomiędzy dwoma zadanymi punktami:
	- Użytkownik może wybrać dwa punkty na aktywnej warstwie.
	- Wtyczka oblicza różnicę wysokości między tymi punktami.
	- Wynik zostaje wyświetlony na pasku informacyjnym interfejsu QGIS.
	- W razie wyboru pojedynczego punktu, wtyczka zwróci błąd.

- Obliczenie pola powierzchni dla conajmiej trzech wybranych punktów:
	- Użytkownik może wybrać minimum trzy punkty na aktywnej warstwie.
	- Wtyczka oblicza pole powierzchni figury na podstawie tych punktów metodą Gaussa.
	- Wynik zostaje wyświetlony na pasku informacyjnym interfejsu QGIS.
	- W razie wyboru dwóch punktów, wtyczka zwróci błąd.


### Dodatkowe opcje
--------------------
- Opracowanie pliku wewnątrz wtyczki:
	- Użytkownik może wskazać układ współrzędnych [1992 lub 2000] pliku do wgrania.
	- Możliwość wybrania i otwarcia pliku tekstowego [.txt lub .csv].
	- Zawartość pliku zostaje załadowana do pamięci podręcznej aplikacji i umieszczona w tabeli (QTableWidget).
	- Dodanie warstwy w odpowiednim układzie odniesienia [EPSG] do bieżącego projektu QGIS.

- Rysowanie poligonu na podstawie zaznaczonych punktów i obliczenie pola powierzchni:
	- Użytkownik może wybrać punkty na aktywnej warstwie, aby utworzyć poligon.
	- Wtyczka rysuje ten poligon i dodaje go do nowej warstwy w projekcie QGIS.
	- Sprawdzenie atrybutu geometry().area() dla porównania z obliczonym polem powierzchni.

- Czyszczenie konsoli wynikowej i zaznaczenia obiektów na żądanie użytkownika.

- Wybór opcji wyświetlania pola powierzchni w m2, arach lub ha zgodnie z wyborem użytkownika.




### Proces instalacyjny
--------------------

1. Pobierz wtyczkę z [url]

2. Otwórz program QGIS.

3. Przejdź do menu "Wtyczki" > "Zarządzaj i zainstaluj wtyczki...".

[ZDJ]

4. Wybierz opcję "Załaduj wtyczkę z pliku..." i wskaż pobrany plik wtyczki.

[ZDJ]

5. Po załadowaniu wtyczki, zostanie ona aktywowana i widoczna w panelu bocznym lub menu QGIS.

[ZDJ]


### Obsługa wtyczki
--------------------

-Obliczenie różnicy wysokości

[GIF]

-Obliczenie pola powierzchni

[GIF]

-Import danych z pliku [.txt lub .csv]

[GIF]

-Dodanie danych do tabeli

[gif]

-Rysowanie poliganu na podstawie punktów

[GIF]

-Monit oraz czyszczenie konsoli

[GIF]

