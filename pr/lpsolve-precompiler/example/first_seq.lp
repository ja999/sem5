min: T;
T > T1;
T > T2;
T > T3;
T > T4;
1000 > d12;
10000 + d12 > d21 + d23 + d24;
Tzk1 = 2 * d12 + 2 * d21;
Trk2 > Tzk3 + -10000000 * x34;
Trk2 > Tzk1;
Trk3 > Tzk2 + -10000000 + 10000000 * x34;
Trk3 > Tzk1;
Tzk2 = Trk2 + 1 * d23;
Tzk3 = Trk3 + 1 * d24;
Tzk > Tzk2;
Tzk > Tzk3;
T1 > Tzk1 + 1000 + -1 * d12 + 1 * d21;
T2 > Tzk + 120000 + 12 * d12 + -12 * d21 + -12 * d23 + -12 * d24;
T3 > Tzk2 + 1 * d23;
T4 > Tzk3 + 2 * d24;
int x34, d12, d21, d23, d24;