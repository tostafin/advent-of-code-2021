#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    vector <string> moves;
    vector <int> values;
    ifstream input("input3");
    string move;
    int value;
    while (input >> move >> value) {
        moves.push_back(move);
        values.push_back(value);
    }

    int horizontalPos = 0, depth = 0;
    for (int i = 0; i < moves.size(); i++) {
        if (moves[i] == "forward") horizontalPos += values[i];
        else if (moves[i] == "down") depth += values[i];
        // else if below just in case we have an invalid input
        else if (moves[i] == "up") depth -= values[i];
    }

    cout << horizontalPos * depth << endl;
}
