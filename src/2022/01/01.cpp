#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main(){
    std::ifstream input("../../../2022/01/input.txt");
    std::string line;

    std::vector<int>values = {};
    int tlt = 0;
    while(std::getline(input, line)){
        if (line.length() == 0){
            values.push_back(tlt);
            tlt = 0;
            continue;
        }
        tlt += std::stoi(line);

    }
    input.close();

    std::sort(values.begin(), values.end(), [](int a, int b){return a>b;});

    std::cout << "Part 1: " << *std::max_element(values.begin(), values.end()) << std::endl;
    std::cout << "Part 2: " << (values[0] + values[1] + values[2]) << std::endl;

    return 0;
}
