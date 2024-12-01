#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>  // For abs()

using namespace std;

int main() {
    string line;
    ifstream dataFile("C:\\Users\\stran\\Documents\\AdventCode2024\\day_1\\input_day_1.txt");

    if (dataFile.is_open()) {
        vector<int> list1, list2;

        while (getline(dataFile, line)) {
            stringstream ss(line); // Parse the line
            int num1, num2;
            ss >> num1 >> num2;
            list1.push_back(num1);
            list2.push_back(num2);
        }
        dataFile.close();

        // Sorting both lists
        sort(list1.begin(), list1.end());
        sort(list2.begin(), list2.end());

        // Part 1: Calculate the total distance
        int distance = 0;
        for (size_t i = 0; i < list1.size(); ++i) {
            distance += abs(list1[i] - list2[i]);
        }

        // Part 2: Calculate the similarity score
        int similarity_score = 0;
        for (const int& num : list1) {
            similarity_score += num * count(list2.begin(), list2.end(), num);
        }

        // Output the results
        cout << "Total Distance: " << distance << endl;
        cout << "Similarity Score: " << similarity_score << endl;
    } else {
        cout << "Unable to open file" << endl;
    }

    return 0;
}
