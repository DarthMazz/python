namespace CSharpDLL
{
    public class Calculation
    {
        public byte[] Result;

        // intの足し算
        public int Add(int a, int b)
        {
            int size = 1024 * 1024 * 10;
            Result = new byte[size];
            for (int i = 0; i < size; i++)
            {
                Result[i] = (byte)'b';
            }
            return a + b;
        }

        // floatの足し算
        public float Add(float a, float b)
        {
            return a + b;
        }

        // stringの足し算(文字列の結合)
        public string Add(string a, string b)
        {
            return a + b;
        }

        // 結果を引数(outの参照渡し)で返す場合
        public bool Add_ref(int a, int b, out int ans)
        {
            ans = a + b;
            return true;
        }

        // 結果を引数(refの参照渡し)で返す場合
        public bool Add_out(int a, int b, ref int ans)
        {
            ans += a + b;
            return true;
        }
    }
}