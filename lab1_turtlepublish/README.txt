Readme.txt

Sposób uruchomienia:

Po pobraniu pakietu należy uruchomić go poleceniem roslaunch lab1_turtlepublish lab1_turtlepublish.launch
Uruchamia to okno zółwia oraz skrypt sterujący. W celu uruchomienia sterowania należy kliknąć w okno uruchomionego skryptu.

Sterowanie:
W - ruch do przodu
A - obrót w lewo
D - obrót w prawo
S - ruch do tyłu

Opis działania programu:
Po uruchomieniu programu publikowany jest log na terminalu o uruchomieniu węzła, następnie jest sprawdzane uruchomienie biblioteki rospy
- jeśli nie wystąpi wyjątek ROSInterruptException, uruchamiana jest metoda turtle_publish, w przeciwnym razie na terminal jest wyświetlany komunikat
 o zakończeniu skryptu turtle_publisher.py.

Po uruchomieniu metody turtle_publish publikowany na terminal jest log o uruchomieniu metody turtle_publish, jest uruchamiana metoda rospy.Publisher służąca
do publikacji na temat /turtle1/cmd_vel, służący do transmisji wiadomości o prędkościach żółwia. Nastęonie jest uruchamiany węzeł turtle_publsih oraz ustalana jest częstotliwosć wysyłania wiadomości(40 Hz, rosPy.rate). Następnie są ustawiane własności biblioteki curses, służącej do odbioru komend z klawiatury

Informacja o tym, jakie przyciski są stosowane do sterowania, pobierane z serwera parametrów ROS, po przejściu całej procedury ustawiania parametrów na terminal jest publikowany log o przejściu ustawień.

W pętli while, działające tak długo, jak uruchomiona jest biblioteka rospy, sprawdzane są przyciski - w zależności od wcisniętego przycisku wykonuje się określony ruch żółwia z zadaną prędkością.

W pliku lab1rosgraph.svg znajduje się graf przedstawiający węzły w paczce w trakcie działania
 



