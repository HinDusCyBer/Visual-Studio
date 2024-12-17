#include <stdio.h>
unsigned int circular_shift_right(unsigned int num, int shift)
{
  unsigned int result = 0;
  for (int i = 0; i < 32; i++)
  {
    int bit = (num & (1 << i)) != 0;
    int target_index = (i - shift + 32) % 32;
    result |= bit << target_index;
  }
  return result;
}
int main()
{
  unsigned int num = 0b1010;
  int shift = 2;
  unsigned int result = circular_shift_right(num, shift);
  printf("The result of a circular shift right of %u by %d positions is: %u\n", num, shift, result);
  return 0;
}