#include <iostream>
using namespace std;
#include <list>
typedef std::list<int> IntList;


int main(void){
int N;
    cin >> N;
int p[N];
for(int i =0;i<N;i++){
    cin >> p[i];
}

int Max = max_element(p)

IntList sample;
for(int i =0; i < Max; i++){
    sample.push_back(i);
}

for(int i =0;i<N;i++){
    sample.erase(p[i])
    cout << p[0] << endl;
}

}
