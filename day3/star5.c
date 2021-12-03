#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    char *line;
    size_t len = 0;
    ssize_t read;
    fp = fopen("input5", "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    ssize_t lineLen = getline(&line, &len, fp) - 1;
    int *zeroCnt = calloc(lineLen, sizeof(int));
    int *oneCnt = calloc(lineLen, sizeof(int));

    while ((read = getline(&line, &len, fp)) != -1) {
        for (int i = 0; i < read - 1; i++) {
            switch (line[i] - '0') {
                case 0:
                    zeroCnt[i]++;
                    break;

                case 1:
                    oneCnt[i]++;
                    break;
            }
        }
    }
    
    char gammaBin[lineLen], epsilonBin[lineLen];
    for (int i = 0; i < lineLen; i++) {
        if (zeroCnt[i] > oneCnt[i]) {
            gammaBin[i] = '0';
            epsilonBin[i] = '1';
        }
        else {
            gammaBin[i] = '1';
            epsilonBin[i] = '0';
        }
    }
    
    int gammaDec = 0, epsilonDec = 0;
    for (int i = 0; i < lineLen; i++) {
        if (gammaBin[i] == '1') gammaDec = 2 * gammaDec + 1;
        else gammaDec *= 2;
        if (epsilonBin[i] == '1') epsilonDec = 2 * epsilonDec + 1;
        else epsilonDec *= 2;

    }
    printf("%d\n", gammaDec * epsilonDec);
    fclose(fp);
    if (line) free(line);
    return 0;
}   


