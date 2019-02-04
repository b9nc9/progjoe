#include <iostream>
#include <string>
#include <set>

using namespace std;


int Szamol(char c, string s){
        int n = 0;
        for(int i = 0; i < s.length(); i++){
                if(s[i] == c){
                        n++;
                }
        }
        return n;
}


int main(){
        set <char, greater <char>> betuk;
        string szo = "ALMA";
        int nyeremenyek[13] = {0, 0, 900, 900, 1700, 2500, 1300, 1100, 3000, 600, 2000, 1500, 1200};
        srand(time(NULL));
        int r = 0;
        for(int i = 0; i < szo.length(); i++){
                betuk.insert(szo[i]);
        }

        int ossz = 0;

        char tipp = ' ';
        while(betuk.size() != 0 && (r != 0 || r != 1)){
                r =  rand() % 13;
                cout << "Tipp: ";
                cin >> tipp;
                ossz += nyeremenyek[r]*Szamol(tipp, szo);
                betuk.erase(tipp);
        }
        if(ossz > 0){
                cout << "Nyertél! \nA nyereményed: " << ossz << " Ft" << endl;
        }
        else{
                cout << "Hát ez csőd...";
        }

        return 0;
}
