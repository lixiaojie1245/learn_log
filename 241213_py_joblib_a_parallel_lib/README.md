```sh
# parallel
time python3 main.py
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465]

real    0m10.382s
user    0m16.878s
sys     0m0.290s
```
```sh
# liner
time python3 main1.py
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465]

real    0m8.661s
user    0m8.633s
sys     0m0.020s
```

# The reason the parallel is slower than a single thread may be that my server has only dual core
