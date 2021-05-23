#include <bits/stdc++.h>
using namespace std;

void output(string label, int count) {
  cout << label << ":";
  while (count > 0) {
    cout << "]";
    count--;
  }
  cout << endl;
}

int main() {
  int A, B;
  cin >> A >> B;

  output("A", A);
  output("B", B);
}
