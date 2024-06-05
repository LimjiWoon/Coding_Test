//io, input, output을 위한 라이브러리
#include <iostream>

//골자가 c와 비슷하지만 명령어가 완전히 다르다.
int main()
{
    //std::cout 는 std 라이브러리에서 ::으로 메서드를 호출한다
    //호출할 메서드는 cout로 다른 곳에서는 print와 동일하다
    //c++은 특이하게 << 로 변수를 받는다
    std::cout << "Hello World!";
    return 0;
}