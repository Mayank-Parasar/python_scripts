#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[]) {
    if(argc > 1) {
        cout << "argc: " << argc << endl;
        cout << argv[1] << endl;
    }

    ofstream out_file;
    out_file.open("output.txt");

    vector<ifstream> ifs_;
    vector<string> line;
    ifs_.resize(argc-1);
    line.resize(argc-1);

    for(int i = 0; i < ifs_.size(); ++i) {
        ifs_[i].open(argv[i+1], std::ifstream::in);
    }
    bool read_all;
    int c;
    while(true) {
        read_all = true;
        // have we read all the files to compiletion
        // if yes then break
        for(int k = 0; k < ifs_.size(); ++k) {
            if(ifs_[k])
                read_all = false;
        }
        if(read_all)
            break;
        for(int k = 0; k < ifs_.size(); ++k) {
            // peek for the end of file character in file
            c = ifs_[k].peek();
            if (!(c == EOF)) {
                if (ifs_[k])
                    getline(ifs_[k], line[k]);
                else
                    line[k] = " ";
            } else {
                line[k] = " ";
            }
        }

        for(int k = 0; k < line.size(); ++k) {
            out_file << line[k] << ", ";
        }
        out_file << endl;

    }

    std::cout << "Hello, World!" << std::endl;
    return 0;
}