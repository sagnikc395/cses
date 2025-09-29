#include <iostream>
using namespace std;

// unsigned int countSetBits(int n){
//   //using kernighan's algorithm
//   unsigned int count = 0;
//   while(n){
//     n &= (n-1);
//     count++;
//   }
//   return count;
// }

int bits_set_table256[256];

void initialize() {
  bits_set_table256[0] = 0;
  for(int i=0;i<256;i++){
    bits_set_table256[i] = (i & 1) + bits_set_table256[i/2];
  }
}

//function to return the count of set bits in n
int countSetBits(int n){
  return (bits_set_table256[n & 0xff] + bits_set_table256[(n >> 8) & 0xff] + bits_set_table256[(n >> 16) & 0xff] + bits_set_table256[n >> 24]);
}



int main(){
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);

  int n;
  cin >> n;
  int counter = 0 ;
  initialize();
  for(int i=1;i<=n;i++){
    counter += countSetBits(i);    
  }
  cout << counter << endl;
    
  return 0;
}
