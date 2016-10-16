/* 
 *  Adapted from the UVA tutorial at UofA
 *  from the programming club website
 *  
 */

#include <iostream>

using namespace std;

int main(){
    int t;
    cin >> t;

    int a, b;
    for (int i=0; i< t; i++){
        
        cin >> a >> b;
        if (a > b){
        cout << ">" << endl;
        }
        else if (a < b){
        cout << "<" << endl;
        }
        else
            cout << "=" << endl;
        
    }
    


}

