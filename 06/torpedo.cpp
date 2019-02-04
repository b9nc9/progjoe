#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

/* Tizedik osztályban téliszünet alatt feladták nekünk ezt a feladatot.
 * Akkoriban, ha jól emlékszek 3 nap alatt sikerült megírnom ezt a játékot C#-ban. Az egész program 382 soros volt.
 * Most mindennel együtt ezt a programot megírtam ~1 óra alatt teljesen a nulláról. A kommentjeim nélkül ezt a programot le tudnám faragni 100 sor alá.
 * Köszönöm szépen a lehetőséget! Most látom először, hogy mennyire jutottam ezalatt a pár év alatt. :)
 * */



/* JELMAGYARÁZAT:
 *      + = talált
 *      - = nem talált
 *      * = semleges
 *     
 * HOGYAN JÁTSZD:
 * - "sor oszlop" alakban add meg a kilőni kívánt koordinátákat!
 * - adj meg 0 0 koordinátákat, ha be akarod fejezni a játékot
 *
 *  */


// OSZTÁLYOK
class Tabla{
        public:
                int hajok[10][10];
                char tabla[10][10];
                Tabla(){
                        srand(time(NULL));
                        for(int i = 0; i < 10; i++){
                                for(int j = 0; j < 10; j++){
                                        tabla[i][j] = '*';
                                        hajok[i][j] = rand() % 2;
                                }
                        }
                
                }
                void Kiir(char (&tabla)[10][10]);
};


class Jatekos{
        private:
                vector<string> talalatok;
        public:
                int Pontok(){return talalatok.size();}
                void Jatek(Tabla &torpedo, Jatekos &jatekos);
                void kiTalalatok(){
                        for(int i = 0; i < talalatok.size(); i++){
                                cout << "| " << talalatok[i] << setw(31) << "|" << endl;
                        }
                        cout << "+----------------------------------+" << endl;

                }
};
// OSZTÁLYOK VÉGE

// FUNKCIÓK
void Tabla::Kiir(char (&tabla)[10][10]){
        cout << "   ¦ 1  2  3  4  5  6  7  8  9  10" << endl;
        cout << "---+------------------------------" << endl;
        for(int i = 0; i < 10; i++){
                cout << setw(3) <<  i+1 << "|";
                for(int j = 0; j < 10; j++){
                       cout << " " << tabla[i][j] << " ";
                }
                cout << "\n";
        }
}


void Jatekos::Jatek(Tabla &torpedo, Jatekos &jatekos){
        int sor = 1;
        int oszlop = 1;
        while(sor != 0){
                torpedo.Kiir(torpedo.tabla);
                cout << "(sor oszlop): ";
                cin >> sor;
                cin >> oszlop;
                if((sor > 0 && sor < 11) && (oszlop > 0 && oszlop < 11)){
                if(torpedo.hajok[sor-1][oszlop-1] == 1){torpedo.tabla[sor-1][oszlop-1] = '+'; jatekos.talalatok.push_back(to_string(sor) + " " + to_string(oszlop));}
                else{torpedo.tabla[sor-1][oszlop-1] = '-';}}
                cout << "\033[2J\033[1;1H";
        }
        cout << "+----------------------------------+" << endl;
        cout << "|           A pontjaid: " << jatekos.talalatok.size() << setw(11) << "|" <<  endl;
        cout << "+----------------------------------+" << endl;
        cout << "|           Eltalált mezők         |" << endl;
        cout << "+----------------------------------+" << endl;
        jatekos.kiTalalatok();
}
// FUNKCIÓK VÉGE

int main(){
        Tabla torpedo = Tabla();
        Jatekos jatekos = Jatekos();
        jatekos.Jatek(torpedo, jatekos);
        return 0;
}


