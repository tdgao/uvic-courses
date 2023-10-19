#include <stdio.h>
#include <string.h>
#define MAX 1500
#include <ctype.h>

// to compile: gcc -Wall -std=c11 -o stop-word-remover stop-word-remover.c

// returns 1 if has stop word, 2 if has stop word with newline
// and returns 0 if there is no stopword
int hasStopWord(char *str)
{
  // defining stop words
  char stopWords[9][10] = {
      "the",
      "a",
      "an",
      "of",
      "for",
      "to",
      "and",
      "but",
      "yet",
  };
  int foundStopWord = 0;

  for (int i = 0; i < 9; i++)
  {
    // get stop word
    char *stopWord = stopWords[i];
    char stopWordNewline[10];
    strcpy(stopWordNewline, stopWord);
    strcat(stopWordNewline, "\n");

    if (!strcmp(str, stopWord))
    {
      foundStopWord = 1;
    }
    else if (!strcmp(str, stopWordNewline))
    {
      foundStopWord = 2;
    }
  }

  return foundStopWord;
}

int main()
{
  // defining buffer and using fgets to take input from stdin
  char input[MAX];
  char filteredString[MAX];

  while (fgets(input, MAX, stdin))
  {
    // set s as the splitter
    const char s[2] = " ";
    char *token;
    token = strtok(input, s);

    while (token != NULL)
    {
      if (!hasStopWord(token))
      {
        // concat filtered tokens to string
        strcat(filteredString, token);

        // only add space if the token does not end with newline
        if (token[strlen(token) - 1] != 10)
        {
          strcat(filteredString, " ");
        }
        // stop word included newline, so add it back
      }
      else if (hasStopWord(token) == 2)
      {
        strcat(filteredString, "\n");
      }

      token = strtok(NULL, s);
    }
  }
  fprintf(stdout, filteredString);

  return 0;
}