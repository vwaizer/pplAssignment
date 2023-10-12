import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_bkel(self):
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_array(self):
        input = """
      main: function void() {
        a: array[2] of integer = {9,5};
      }
      """
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(9), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_array2(self):
        input = """
      main: function void() {
        a: array[2] of string = {"hi","abc\\r"};
      }
      """
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], StringType), ArrayLit([StringLit(hi), StringLit(abc\\r)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_array3(self):
        input = """
      main: function void() {
        a: array[2] of string = {"hi\\"HELLO\\"","abc\\r"};
        return;
      }
      """
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], StringType), ArrayLit([StringLit(hi\\"HELLO\\"), StringLit(abc\\r)])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_array4(self):
        input = """
      foo: function string() {
        return "HI";
      }
      main: function void() {
        a: array[3] of string = {"hi\\"HELLO\\"","abc\\r", foo()};
        return;
      }
      """
        expect = """Program([
\tFuncDecl(foo, StringType, [], None, BlockStmt([ReturnStmt(StringLit(HI))]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], StringType), ArrayLit([StringLit(hi\\"HELLO\\"), StringLit(abc\\r), FuncCall(foo, [])])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_array5(self):
        input = """bool_arr: array[2] of boolean = {true,false};"""
        expect = """Program([
	VarDecl(bool_arr, ArrayType([2], BooleanType), ArrayLit([BooleanLit(True), BooleanLit(False)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_lit(self):
        input = """
      main: function void() {
        a: integer = 12;
        b: boolean = true;
      }
      """
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(12)), VarDecl(b, BooleanType, BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_lit2(self):
        input = """
      main: function void() {
        a: integer = 12;
        b: boolean = true || false ;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(12)), VarDecl(b, BooleanType, BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_lit3(self):
        input = """
      main: function void() {
        a: integer = 123_23;
        b: boolean = false && true;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(12323)), VarDecl(b, BooleanType, BinExpr(&&, BooleanLit(False), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_lit4(self):
        input = """
      main: function void() {
        a: float = 123_23e12 + 23_3E-23;
        b: boolean = false && true;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, BinExpr(+, FloatLit(1.2323e+16), FloatLit(2.33e-21))), VarDecl(b, BooleanType, BinExpr(&&, BooleanLit(False), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_lit5(self):
        input = """
      main: function void() {
        a: float = 123_23e12 - 23_3E-23;
        b: float = .e-25;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, BinExpr(-, FloatLit(1.2323e+16), FloatLit(2.33e-21))), VarDecl(b, FloatType, FloatLit(0.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_lit6(self):
        input = """
      main: function void() {
        a: float = 123_23e12 * 23_3E-23;
        b: float = 2.e-3;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, BinExpr(*, FloatLit(1.2323e+16), FloatLit(2.33e-21))), VarDecl(b, FloatType, FloatLit(0.002))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_lit7(self):
        input = """
      main: function void() {
        a: float = 123_23e12 / 23_3E-23;
        b: float = 2.e-3;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, BinExpr(/, FloatLit(1.2323e+16), FloatLit(2.33e-21))), VarDecl(b, FloatType, FloatLit(0.002))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_lit8(self):
        input = """
      main: function void() {
        a: float = 123_23e12 % 23_3E-23;
        b: float = 2.e-3;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, BinExpr(%, FloatLit(1.2323e+16), FloatLit(2.33e-21))), VarDecl(b, FloatType, FloatLit(0.002))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_lit9(self):
        input = """
      main: function void() {
        a: float = 123_23e12 % 23_3E-23;
        b: float = 2.e-3 - 123 + 23_2;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, BinExpr(%, FloatLit(1.2323e+16), FloatLit(2.33e-21))), VarDecl(b, FloatType, BinExpr(+, BinExpr(-, FloatLit(0.002), IntegerLit(123)), IntegerLit(232)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_lit10(self):
        input = """
      str_ret: function void(){
        a: float = 12.0;
        c: integer;
        b: boolean;
        return;}"""
        expect = """Program([
\tFuncDecl(str_ret, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(12.0)), VarDecl(c, IntegerType), VarDecl(b, BooleanType), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_lit11(self):
        input = """
      str_ret: function void(){
        a: float = 12.0;
        c: integer;
        b: boolean;
        d: string;
        return;}"""
        expect = """Program([
\tFuncDecl(str_ret, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(12.0)), VarDecl(c, IntegerType), VarDecl(b, BooleanType), VarDecl(d, StringType), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_complex(self):
        input = """
            main: function void(){
        x: integer = 12;
        if(x+2==0) return;
        else x = x+1;
        for(i=1,i<10,i+1){
          writeInt(i);
        }
        return;
      }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(12)), IfStmt(BinExpr(==, BinExpr(+, Id(x), IntegerLit(2)), IntegerLit(0)), ReturnStmt(), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_simp4(self):
        input = r"""
      main: function void(){
        x: string = "HI BRP \\asdasdasd";
        if( x=="TEST") return;
        else x = "HAHAHAHHA";
        for(i=1,i<10,i+1){
          foo(i);
        }
        return;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit(HI BRP \\\\asdasdasd)), IfStmt(BinExpr(==, Id(x), StringLit(TEST)), ReturnStmt(), AssignStmt(Id(x), StringLit(HAHAHAHHA))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(foo, Id(i))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_simp5(self):
        input = r"""
          main: function integer(){
            x: integer = readInt();
            if(x+2%3-11+99!=0) return;
            else x = x+1;
            for(i=1,i<10,i+1){
              printInteger(arr[i,i]);
            }
            return x+3;
          }
          """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(x, IntegerType, FuncCall(readInt, [])), IfStmt(BinExpr(!=, BinExpr(+, BinExpr(-, BinExpr(+, Id(x), BinExpr(%, IntegerLit(2), IntegerLit(3))), IntegerLit(11)), IntegerLit(99)), IntegerLit(0)), ReturnStmt(), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(arr, [Id(i), Id(i)]))])), ReturnStmt(BinExpr(+, Id(x), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_simp6(self):
        input = r"""
      foo: function integer(x: integer){
        return x*2;
      }
      main: function void(){
        foo(23);
      }
      """
        expect = """Program([
\tFuncDecl(foo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), IntegerLit(2)))]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(23))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_expression(self):
        input = r"""
      main:function void(){
        x: integer = -2+3-123*12_9;
        y: float = 2e13-23;
        a: integer = 12;
        z: string = "NICE NICE NICE \t\t\f\f\f\r";
        s: boolean = !false && true;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, BinExpr(-, BinExpr(+, UnExpr(-, IntegerLit(2)), IntegerLit(3)), BinExpr(*, IntegerLit(123), IntegerLit(129)))), VarDecl(y, FloatType, BinExpr(-, FloatLit(20000000000000.0), IntegerLit(23))), VarDecl(a, IntegerType, IntegerLit(12)), VarDecl(z, StringType, StringLit(NICE NICE NICE \\t\\t\\f\\f\\f\\r)), VarDecl(s, BooleanType, BinExpr(&&, UnExpr(!, BooleanLit(False)), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_expression2(self):
        input = r"""
      main: function void(){
        if(true) return;
        else return;
        x: array [2] of integer = {123_232323,-232323_23232};
      }
      """
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ReturnStmt(), ReturnStmt()), VarDecl(x, ArrayType([2], IntegerType), ArrayLit([IntegerLit(123232323), UnExpr(-, IntegerLit(23232323232))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_expression3(self):
        input = r"""
      main: function void() {
        /*
        asoasdjasj dklasjkld jklasjldjlas
        asdaksjdklajslkd jasd
        sjad kjask ljdklaj kldjklsajdlk
        asdkajsldjasd
        */
        printInteger(12);
      }
      """
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_expression4(self):
        input = r"""
      main: function void() {
        /*
        test multiple line
        */
        // oh yeah
        printInteger(12); // same line comment
      }
      """
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_expression5(self):
        input = r"""
      main: function void() {
        /*
        test multiple line
        */
        // oh yeah
        x: integer = 12;
        do{
          if(x!=25) x = x+1;
          else break;
        }while(true);
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(12)), DoWhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(!=, Id(x), IntegerLit(25)), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_expression6(self):
        input = r"""
      main: function void() {
        /*
        test multiple line
        */
        // oh yeah
        x: integer = 12_123123 + -903203_123;
        do{
          if(x!=25) x = x / 2;
          else break;
          printInteger(x);
          // test comment in block again
        }while(true);
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, BinExpr(+, IntegerLit(12123123), UnExpr(-, IntegerLit(903203123)))), DoWhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(!=, Id(x), IntegerLit(25)), AssignStmt(Id(x), BinExpr(/, Id(x), IntegerLit(2))), BreakStmt()), CallStmt(printInteger, Id(x))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_expression7(self):
        input = r"""
      main: function void() {
        /*
        test multiple line
        */
        // oh yeah
        x: string = "abc";
        do{
          x = x::"def";
          if(x == "abcdefghijklmnop") break;
          else x=x::"ghijklmnop";
        }while(true);
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit(abc)), DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(x), StringLit(def))), IfStmt(BinExpr(==, Id(x), StringLit(abcdefghijklmnop)), BreakStmt(), AssignStmt(Id(x), BinExpr(::, Id(x), StringLit(ghijklmnop))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_expression8(self):
        input = r"""
      main: function void() {
        /*
        test multiple linep
        aslasdklasd
        asdklasdklas
        kasldasd
        */
        // oh yeah
        x: string = "abc123123asd";
        do{
          /*
          cp,,emt om ;pp[s]
          */
          x = x::"def";
          if(x == "abcdefghijklmnop") break;
          x = x::"123123";
        }while(true);
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit(abc123123asd)), DoWhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(x), BinExpr(::, Id(x), StringLit(def))), IfStmt(BinExpr(==, Id(x), StringLit(abcdefghijklmnop)), BreakStmt()), AssignStmt(Id(x), BinExpr(::, Id(x), StringLit(123123)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_expression9(self):
        input = r"""
        foo:function string() {
          return "ABC \t\t";
        }
        bar: function string() {
          return "DEFEFEFEF\r\r\r\b\b\b";
        }
      main: function void() {
        /*
        test multiple linep
        aslasdklasd
        asdklasdklas
        kasldasd
        */
        // oh yeah
        x: string = foo();
        y: string = bar();
        z: string = x::y;
      }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [], None, BlockStmt([ReturnStmt(StringLit(ABC \\t\\t))]))
	FuncDecl(bar, StringType, [], None, BlockStmt([ReturnStmt(StringLit(DEFEFEFEF\\r\\r\\r\\b\\b\\b))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, FuncCall(foo, [])), VarDecl(y, StringType, FuncCall(bar, [])), VarDecl(z, StringType, BinExpr(::, Id(x), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_expression10(self):
        input = r"""
        foo:function string() {
          return "ABC \t\t";
        }
        bar: function string() {
          return "DEFEFEFEF\r\r\r\b\b\b";
        }
      main: function void() {
        /*
        test multiple linep
        aslasdklasd
        asdklasdklas
        kasldasd
        */
        // oh yeah
        x: string = foo();
        y: string = bar();
        z: string = x::y;
        if(x==y) return;
        else if(z==y) return;
        else return;
      }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [], None, BlockStmt([ReturnStmt(StringLit(ABC \\t\\t))]))
	FuncDecl(bar, StringType, [], None, BlockStmt([ReturnStmt(StringLit(DEFEFEFEF\\r\\r\\r\\b\\b\\b))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, FuncCall(foo, [])), VarDecl(y, StringType, FuncCall(bar, [])), VarDecl(z, StringType, BinExpr(::, Id(x), Id(y))), IfStmt(BinExpr(==, Id(x), Id(y)), ReturnStmt(), IfStmt(BinExpr(==, Id(z), Id(y)), ReturnStmt(), ReturnStmt()))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_sth2(self):
        input = r"""
      main: function void() {
        arr: array [3] of string = {"abc", "\r\r\r\f\f\f\f\f\fGREAT"};
        for(i=0,i<3,i+1){
          print(arr[i]);
        }
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], StringType), ArrayLit([StringLit(abc), StringLit(\\r\\r\\r\\f\\f\\f\\f\\f\\fGREAT)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, ArrayCell(arr, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_sth3(self):
        input = r"""
      main: function void() {
        arr: array [3] of string = {"abc", "def", "E"};
        big_str: string = "";
        for(i=0,i<3,i+1){
          big_str = big_str :: arr[i];
        }
        print(big_str);
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], StringType), ArrayLit([StringLit(abc), StringLit(def), StringLit(E)])), VarDecl(big_str, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(big_str), BinExpr(::, Id(big_str), ArrayCell(arr, [Id(i)])))])), CallStmt(print, Id(big_str))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_bkel2(self):
        input = """
      main:function void() {
        foo(5*3-12);
        foobar("hiiii");
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(-, BinExpr(*, IntegerLit(5), IntegerLit(3)), IntegerLit(12))), CallStmt(foobar, StringLit(hiiii))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_simple_program_again(self):
        input = """main: function void() {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_simple_2(self):
        input = """
      test: function integer() {
        return 2+3;
      }
      """
        expect = """Program([
	FuncDecl(test, IntegerType, [], None, BlockStmt([ReturnStmt(BinExpr(+, IntegerLit(2), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_simple3(self):
        input = """test: function float(){return 2_3e+3;}"""
        expect = """Program([
\tFuncDecl(test, FloatType, [], None, BlockStmt([ReturnStmt(FloatLit(23000.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_simple4(self):
        input = """asd: function void(){
        return 2_3 + 3.2 - 49;
      }"""
        expect = """Program([
	FuncDecl(asd, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(-, BinExpr(+, IntegerLit(23), FloatLit(3.2)), IntegerLit(49)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_multi_array(self):
        input = """arr1,arr2: array[2,2] of integer = {{1,23},{33,4}},{{4,35},{5,6}};"""
        expect = """Program([
	VarDecl(arr1, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(23)]), ArrayLit([IntegerLit(33), IntegerLit(4)])]))
	VarDecl(arr2, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(4), IntegerLit(35)]), ArrayLit([IntegerLit(5), IntegerLit(6)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_simple6(self):
        input = r"""
      str_ret: function string(){
        return "abc \"hi\"";
      }"""
        expect = """Program([
	FuncDecl(str_ret, StringType, [], None, BlockStmt([ReturnStmt(StringLit(abc \\"hi\\"))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_simple7(self):
        input = r"""
      str_ret: function string(){
        return "abc\"hi\""::"NICE";
      }"""
        expect = """Program([
	FuncDecl(str_ret, StringType, [], None, BlockStmt([ReturnStmt(BinExpr(::, StringLit(abc\\"hi\\"), StringLit(NICE)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_simple8(self):
        input = r"""
      str_ret: function string(){
        return "abc \"hi\r\r\r\b\b\n\'\t\t\f\f\b\n\"";
      }"""
        expect = """Program([
	FuncDecl(str_ret, StringType, [], None, BlockStmt([ReturnStmt(StringLit(abc \\"hi\\r\\r\\r\\b\\b\\n\\'\\t\\t\\f\\f\\b\\n\\"))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_simple9(self):
        input = r"""
      str_ret: function integer(){
        a: integer = 12_32323232323232323;
        b: array [1] of integer = 123;
        return a+23-23231123%123*9999;
      }"""
        expect = """Program([
	FuncDecl(str_ret, IntegerType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1232323232323232323)), VarDecl(b, ArrayType([1], IntegerType), IntegerLit(123)), ReturnStmt(BinExpr(-, BinExpr(+, Id(a), IntegerLit(23)), BinExpr(*, BinExpr(%, IntegerLit(23231123), IntegerLit(123)), IntegerLit(9999))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_other(self):
        input = r"""
        a: integer;
        b,c: integer;
        e,f,g: float;
        d: array [1] of integer;
      """
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	VarDecl(e, FloatType)
	VarDecl(f, FloatType)
	VarDecl(g, FloatType)
	VarDecl(d, ArrayType([1], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_other2(self):
        input = r"""
      a,b: string = "hi", "YO \"bro\"";
      """
        expect = """Program([
	VarDecl(a, StringType, StringLit(hi))
	VarDecl(b, StringType, StringLit(YO \\"bro\\"))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_other3(self):
        input = r"""
      // hey
      a: integer = 123_123123_123123123213123;
      """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(123123123123123123213123))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_bkel213(self):
        input = r"""
        x: integer = 65;
          fact: function integer (n: integer) {
              if (n == 0) return 1;
              else return n * fact(n - 1);
          }
          inc: function void(out n: integer, delta: integer) {
              n = n + delta;
          }
          main: function void() {
              delta: integer = fact(3);
              inc(x, delta);
              printInteger(x);
          }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_xamp8(self):
        input = r"""
        return_string: function string() {
          return "hello world";
        }
      main:function void(){
        a: array [2] of string = {foo(), foo()};
        i: integer = 0;
        while(i<2){
          print(a[i]);
          i = i+1;
        }
      return;}"""
        expect = """Program([
	FuncDecl(return_string, StringType, [], None, BlockStmt([ReturnStmt(StringLit(hello world))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], StringType), ArrayLit([FuncCall(foo, []), FuncCall(foo, [])])), VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), IntegerLit(2)), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_xamp9(self):
        input = r"""
        return_string: function string() {
          return "hello world";
        }
      main:function void(){
        a: array [2] of string = {foo(), foo()};
        i: integer = 0;
        while(i<2){
          print(a[i]);
          if(i == 1) {
            i = 0;
            break;
          }
          i = i+1;
        }
      }"""
        expect = """Program([
	FuncDecl(return_string, StringType, [], None, BlockStmt([ReturnStmt(StringLit(hello world))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], StringType), ArrayLit([FuncCall(foo, []), FuncCall(foo, [])])), VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), IntegerLit(2)), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i)])), IfStmt(BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), IntegerLit(0)), BreakStmt()])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_xamp10(self):
        input = r"""
        return_string: function string() {
          return "hello world";
        }
      main:function void(){
        // FILE NAY THUOC VE HOANG NGUYEN 2052619
        a: array [2] of string = {foo(), foo()};
        i: integer = 0;
        while(i<2){
          print(a[i]);
          if(i == 1) {
            i = 0;
            break;
            continue;
            return;
          }
          i = i+1;
        }
      }"""
        expect = """Program([
	FuncDecl(return_string, StringType, [], None, BlockStmt([ReturnStmt(StringLit(hello world))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], StringType), ArrayLit([FuncCall(foo, []), FuncCall(foo, [])])), VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), IntegerLit(2)), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i)])), IfStmt(BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), IntegerLit(0)), BreakStmt(), ContinueStmt(), ReturnStmt()])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_simple7again(self):
        input = """
      main: function void() {
        a: array [2,3] of integer = {{2,3,2},{1,2,3}};
        for(i=0,i<2,i+1){
          for(j=0,j<3,j+1){
            print(a[i,j]);
          }
        }
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i), Id(j)]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_simple8again(self):
        input = """
      main: function void() {
        a: array [2,3] of string = {{"YEUEM","GHETEM","TUEM"},{"OH YEAH","QUA TUYET","AMAZING"}};
        for(i=0,i<2,i+1){
          for(j=0,j<3,j+1){
            print(a[i,j]);
          }
        }
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(YEUEM), StringLit(GHETEM), StringLit(TUEM)]), ArrayLit([StringLit(OH YEAH), StringLit(QUA TUYET), StringLit(AMAZING)])])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(print, ArrayCell(a, [Id(i), Id(j)]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_simple3_again(self):
        input = """
      main: function void(){
        // comment here asdasd jaskdj klajsd 
        /*
        sadasd
        as
        das
        d
        asd
        as
        asd
        */
        x: float = 2.0e12;
        writeFloat(-x);

      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(2000000000000.0)), CallStmt(writeFloat, UnExpr(-, Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_lit_again(self):
        input = """x: float = 23_3e-23;"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(2.33e-21))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_lit_again2(self):
        input = """
      main: function void(){
        a = b;
      }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_xamp11(self):
        input = r"""
        foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

      main:function void(){
        print("FINALLY FINISH EVERYTHING");
      }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(FINALLY FINISH EVERYTHING))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_xamp(self):
        input = r"""main:function void(){
        a: integer = 23+23-33_2%90;
        b: float = 23_2_3_23.2e23;
        printInteger(a);
        writeFloat(b);
      return;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(23), IntegerLit(23)), BinExpr(%, IntegerLit(332), IntegerLit(90)))), VarDecl(b, FloatType, FloatLit(2.323232e+28)), CallStmt(printInteger, Id(a)), CallStmt(writeFloat, Id(b)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_xamp2(self):
        input = r"""main:function void(){
        a: integer = 23+23-33_2%90;
        b: float = 23_2_3_23.2e23 - 23_2_2.E+23;
        printInteger(a);
        writeFloat(b);
      return;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(23), IntegerLit(23)), BinExpr(%, IntegerLit(332), IntegerLit(90)))), VarDecl(b, FloatType, BinExpr(-, FloatLit(2.323232e+28), FloatLit(2.322e+26))), CallStmt(printInteger, Id(a)), CallStmt(writeFloat, Id(b)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_xamp3(self):
        input = r"""
      foo:function float() {
        return 123_323_3.e-23;
      }
      main:function void(){
        a: integer = 23+23-33_2%90;
        b: float = 23_2_3_23.2e23 - 23_2_2.E+23 - foo();
        printInteger(a);
        writeFloat(b);
      return;}"""
        expect = """Program([
	FuncDecl(foo, FloatType, [], None, BlockStmt([ReturnStmt(FloatLit(1.233233e-17))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(23), IntegerLit(23)), BinExpr(%, IntegerLit(332), IntegerLit(90)))), VarDecl(b, FloatType, BinExpr(-, BinExpr(-, FloatLit(2.323232e+28), FloatLit(2.322e+26)), FuncCall(foo, []))), CallStmt(printInteger, Id(a)), CallStmt(writeFloat, Id(b)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_xamp4(self):
        input = r"""
      foo:function float() {
        return 123_323_3.e-23;
      }
      bar: function float() {
        return foo();
      }
      main:function void(){
        a: integer = 23+23-33_2%90;
        b: float = 23_2_3_23.2e23 - 23_2_2.E+23 - foo() * bar();
        printInteger(a);
        writeFloat(b);
      return;}"""
        expect = """Program([
	FuncDecl(foo, FloatType, [], None, BlockStmt([ReturnStmt(FloatLit(1.233233e-17))]))
	FuncDecl(bar, FloatType, [], None, BlockStmt([ReturnStmt(FuncCall(foo, []))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(23), IntegerLit(23)), BinExpr(%, IntegerLit(332), IntegerLit(90)))), VarDecl(b, FloatType, BinExpr(-, BinExpr(-, FloatLit(2.323232e+28), FloatLit(2.322e+26)), BinExpr(*, FuncCall(foo, []), FuncCall(bar, [])))), CallStmt(printInteger, Id(a)), CallStmt(writeFloat, Id(b)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_xamp5(self):
        input = r"""
      foo:function float() {
        return 123_323_3.e-23;
      }
      bar: function float() {
        return foo();
      }
      main:function void(){
        a: integer = 23%2+23-33_2%90;
        z: boolean = true && false;
        b: float = 23_2_3_23.2e23 - 23_2_2.E+23 - foo() * bar();
        printInteger(a);
        writeFloat(b);
        if(z==true) {
          print("TRUE");
        }
      return;}"""
        expect = """Program([
	FuncDecl(foo, FloatType, [], None, BlockStmt([ReturnStmt(FloatLit(1.233233e-17))]))
	FuncDecl(bar, FloatType, [], None, BlockStmt([ReturnStmt(FuncCall(foo, []))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, BinExpr(%, IntegerLit(23), IntegerLit(2)), IntegerLit(23)), BinExpr(%, IntegerLit(332), IntegerLit(90)))), VarDecl(z, BooleanType, BinExpr(&&, BooleanLit(True), BooleanLit(False))), VarDecl(b, FloatType, BinExpr(-, BinExpr(-, FloatLit(2.323232e+28), FloatLit(2.322e+26)), BinExpr(*, FuncCall(foo, []), FuncCall(bar, [])))), CallStmt(printInteger, Id(a)), CallStmt(writeFloat, Id(b)), IfStmt(BinExpr(==, Id(z), BooleanLit(True)), BlockStmt([CallStmt(print, StringLit(TRUE))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_xamp6(self):
        input = r"""
      main:function void(){
        /**/
        a: integer = 23%2+23-33_2%90;
        z: boolean = true && false;
        printInteger(a);
        writeFloat(z);
        // ASJDASJDAJSDJASJD
        if(z==true) {
          print("TRUE");
        }else {
          print("FALSE");
        }
      return;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(-, BinExpr(+, BinExpr(%, IntegerLit(23), IntegerLit(2)), IntegerLit(23)), BinExpr(%, IntegerLit(332), IntegerLit(90)))), VarDecl(z, BooleanType, BinExpr(&&, BooleanLit(True), BooleanLit(False))), CallStmt(printInteger, Id(a)), CallStmt(writeFloat, Id(z)), IfStmt(BinExpr(==, Id(z), BooleanLit(True)), BlockStmt([CallStmt(print, StringLit(TRUE))]), BlockStmt([CallStmt(print, StringLit(FALSE))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_xamp7(self):
        input = r"""
        foo: function string() {
          return "hello world";
        }
      main:function void(){
        a: array [2] of string = {foo(), foo()};
      return;}"""
        expect = """Program([
	FuncDecl(foo, StringType, [], None, BlockStmt([ReturnStmt(StringLit(hello world))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2], StringType), ArrayLit([FuncCall(foo, []), FuncCall(foo, [])])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_some(self):
        input = """
      main: function void() {
        arr: array [5] of integer = {1_123123123, 45_45, -123, 2+3, 123};
        for(i = 0,i<5,i+1){
          printInteger(arr[i]);
        }
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1123123123), IntegerLit(4545), UnExpr(-, IntegerLit(123)), BinExpr(+, IntegerLit(2), IntegerLit(3)), IntegerLit(123)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(arr, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_some2(self):
        input = """
      main: function void() {
        arr: array [5] of float = {1_123123123e213, 45_45.2, -123.6, 2.2+3.3, 123E+123};
        for(i = 0,i<5,i+1){
          writeFloat(arr[i]);
        }
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([5], FloatType), ArrayLit([FloatLit(1.123123123e+222), FloatLit(4545.2), UnExpr(-, FloatLit(123.6)), BinExpr(+, FloatLit(2.2), FloatLit(3.3)), FloatLit(1.23e+125)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeFloat, ArrayCell(arr, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_some3(self):
        input = """
      main: function void() {
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_some4(self):
        input = """
      main: function void() {
        r, s: integer;
        r = 2.0;
        a, b: array [5] of integer;
        s = r * r * myPI;
        a[b[0]] = s;
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [ArrayCell(b, [IntegerLit(0)])]), Id(s))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_some5(self):
        input = """
      main: function void() {
        x: integer = 123;
        while(x!=0){
          if(x%2==0) x = x/2;
          else x = x-1;
          if(x%3==0) break;
          else continue;
        }
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(123)), WhileStmt(BinExpr(!=, Id(x), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), AssignStmt(Id(x), BinExpr(/, Id(x), IntegerLit(2))), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1)))), IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(3)), IntegerLit(0)), BreakStmt(), ContinueStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_some6(self):
        input = """
      main: function void() {
        foo(bar(foobar()));
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, FuncCall(bar, [FuncCall(foobar, [])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_some7(self):
        input = """
      foo: function integer(out x: integer){
        /*
        I am just a comment but multiple line
        */
        return x*2;
      }
      main: function void() {
        x: integer = foo(2);
        z: integer = foo(x + foo(4));
      }
      """
        expect = """Program([
	FuncDecl(foo, IntegerType, [OutParam(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), IntegerLit(2)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, FuncCall(foo, [IntegerLit(2)])), VarDecl(z, IntegerType, FuncCall(foo, [BinExpr(+, Id(x), FuncCall(foo, [IntegerLit(4)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_some8(self):
        input = """
      main: function void() {
        for(i=0,!(x<0),i-5){
          printInteger(i);
        }
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), UnExpr(!, BinExpr(<, Id(x), IntegerLit(0))), BinExpr(-, Id(i), IntegerLit(5)), BlockStmt([CallStmt(printInteger, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_some9(self):
        input = """
      main: function void() {
        for(i=0,!(x<0),i-5){
          if((i!=12) || (i==0)){
            printInteger(i);
          }
        }
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), UnExpr(!, BinExpr(<, Id(x), IntegerLit(0))), BinExpr(-, Id(i), IntegerLit(5)), BlockStmt([IfStmt(BinExpr(||, BinExpr(!=, Id(i), IntegerLit(12)), BinExpr(==, Id(i), IntegerLit(0))), BlockStmt([CallStmt(printInteger, Id(i))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_sth4(self):
        input = r"""
      main: function void() {
        arr: array [3] of string = {"abc", "def", "E"};
        big_str: string = "";
        for(i=0,i<3,i+1){
          // concat then print
          big_str = big_str :: arr[i];
          print(big_str);
          if(big_str == "") print("INVALID");
          else continue;
        }
        // clear string after needed
        big_str = "";
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], StringType), ArrayLit([StringLit(abc), StringLit(def), StringLit(E)])), VarDecl(big_str, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(big_str), BinExpr(::, Id(big_str), ArrayCell(arr, [Id(i)]))), CallStmt(print, Id(big_str)), IfStmt(BinExpr(==, Id(big_str), StringLit()), CallStmt(print, StringLit(INVALID)), ContinueStmt())])), AssignStmt(Id(big_str), StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_sth5(self):
        input = r"""
      main: function void() {
        arr: array [3] of string = {"abc", "def", "laskdlkasdklaskld"};
        big_str: string = "";
        for(i=0,i<3,i+1){
          // concat then print
          big_str = big_str :: arr[i];
          while(big_str != ""){
            break;
          }
        }
        // clear string after needed
        big_str = "";
        print("PROGRAM FINISH");
      }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], StringType), ArrayLit([StringLit(abc), StringLit(def), StringLit(laskdlkasdklaskld)])), VarDecl(big_str, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(big_str), BinExpr(::, Id(big_str), ArrayCell(arr, [Id(i)]))), WhileStmt(BinExpr(!=, Id(big_str), StringLit()), BlockStmt([BreakStmt()]))])), AssignStmt(Id(big_str), StringLit()), CallStmt(print, StringLit(PROGRAM FINISH))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_sth6(self):
        input = r"""
        foo:function integer(){
          return 23;
        }
      main: function void() {
        arr: array [3] of string = {"abc", "def", "laskdlkasdklaskld"};
        big_str: string = "";
        x: integer = foo();
        for(i=0,i<3,i+1){
          // concat then print
          big_str = big_str :: arr[i];
          while(big_str != ""){
            if(x==30) break;
            else x = x+1;
          }
        }
        // clear string after needed
        big_str = "";
        print("PROGRAM FINISH");
      }
      """
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(23))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], StringType), ArrayLit([StringLit(abc), StringLit(def), StringLit(laskdlkasdklaskld)])), VarDecl(big_str, StringType, StringLit()), VarDecl(x, IntegerType, FuncCall(foo, [])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(big_str), BinExpr(::, Id(big_str), ArrayCell(arr, [Id(i)]))), WhileStmt(BinExpr(!=, Id(big_str), StringLit()), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(30)), BreakStmt(), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))))]))])), AssignStmt(Id(big_str), StringLit()), CallStmt(print, StringLit(PROGRAM FINISH))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_sth7(self):
        input = r"""
      main: function integer(){
        x: integer = 12;
        do{
          if(x <= 20) x = x+1;
          else break;
        }while(true);
        return 2_333 + -123;
      }
      """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(12)), DoWhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(<=, Id(x), IntegerLit(20)), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), BreakStmt())])), ReturnStmt(BinExpr(+, IntegerLit(2333), UnExpr(-, IntegerLit(123))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_sth8(self):
        input = r"""
        foo: function string(out x: string){
          z: string            = "abc";
          return z::x;
        }
        main:function void(){
          a: string = foo("ASDASDASDASD\f");
          print(a);
        }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [OutParam(x, StringType)], None, BlockStmt([VarDecl(z, StringType, StringLit(abc)), ReturnStmt(BinExpr(::, Id(z), Id(x)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, FuncCall(foo, [StringLit(ASDASDASDASD\\f)])), CallStmt(print, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_sth9(self):
        input = r"""
        foo: function string(out x: string){
          z: string            = "abc";
          return z::x;
        }
        main:function void(){
          print(foo("ASDASDASDASDASDASDASDASDASD\fffff"));
        }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [OutParam(x, StringType)], None, BlockStmt([VarDecl(z, StringType, StringLit(abc)), ReturnStmt(BinExpr(::, Id(z), Id(x)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(foo, [StringLit(ASDASDASDASDASDASDASDASDASD\\fffff)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_sth10(self):
        input = r"""
        foo: function string(out x: string){
          z: string            = "abc";
          return z::x;
        }
        main:function void(){
          print(foo(foo("TEST")));
        }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [OutParam(x, StringType)], None, BlockStmt([VarDecl(z, StringType, StringLit(abc)), ReturnStmt(BinExpr(::, Id(z), Id(x)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(foo, [FuncCall(foo, [StringLit(TEST)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_sth11(self):
        input = r"""
        foo: function string(out x: string){
          z: string            = "abc";
          return z::x;
        }
        main:function void(){
          print(foo(foo(foo(foo(foo("ASDASD\f\f\f\f\\r\r\r\r\\r\r\r\r\\r"))))));
        }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [OutParam(x, StringType)], None, BlockStmt([VarDecl(z, StringType, StringLit(abc)), ReturnStmt(BinExpr(::, Id(z), Id(x)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(foo, [FuncCall(foo, [FuncCall(foo, [FuncCall(foo, [FuncCall(foo, [StringLit(ASDASD\\f\\f\\f\\f\\\\r\\r\\r\\r\\\\r\\r\\r\\r\\\\r)])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_sth12(self):
        input = r"""
        foo: function string(out x: string){
          z: string            = "abc"; // comment ehre 
          return z::x;
          /*
          another comment here xD
          */
        }
        main:function void(){
          z: string = foo("ABC");
          if(z=="ABCabc") return;
          else do{
            if(z=="abc") break;
          }while(true);
        }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [OutParam(x, StringType)], None, BlockStmt([VarDecl(z, StringType, StringLit(abc)), ReturnStmt(BinExpr(::, Id(z), Id(x)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(z, StringType, FuncCall(foo, [StringLit(ABC)])), IfStmt(BinExpr(==, Id(z), StringLit(ABCabc)), ReturnStmt(), DoWhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(==, Id(z), StringLit(abc)), BreakStmt())])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_sth13(self):
        input = r"""
        foo: function string(out x: string){
          z: string            = "abc"; // comment ehre 
          return z::x;
          /*
          another comment here xD
          */
        }
        main:function void(){
          z: string = foo("ABC");
          do{
            for(i=1,i<=10,i+2){
              printInteger(i);
            }
            break;
          }while(true);
        }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [OutParam(x, StringType)], None, BlockStmt([VarDecl(z, StringType, StringLit(abc)), ReturnStmt(BinExpr(::, Id(z), Id(x)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(z, StringType, FuncCall(foo, [StringLit(ABC)])), DoWhileStmt(BooleanLit(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([CallStmt(printInteger, Id(i))])), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_sth14(self):
        input = r"""
        foo: function string(out x: string){
          z: string            = "abc"; // comment ehre 
          return z::x;
          /*
          another comment here xD
          */
        }
        main:function void(){
          z: string = foo("ABC");
          do{
            if(z=="ABCabc")
              while(false){
                //do nothing here
              }
            else for(i=1,i<=10,i+2){
              printInteger(i);
            }
            break;
          }while(true);
        }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [OutParam(x, StringType)], None, BlockStmt([VarDecl(z, StringType, StringLit(abc)), ReturnStmt(BinExpr(::, Id(z), Id(x)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(z, StringType, FuncCall(foo, [StringLit(ABC)])), DoWhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(==, Id(z), StringLit(ABCabc)), WhileStmt(BooleanLit(False), BlockStmt([])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([CallStmt(printInteger, Id(i))]))), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_sth15(self):
        input = r"""
        foo: function string(out x: string){
          z: string            = "abc"; // comment ehre 
          return z::x;
          /*
          another comment here xD
          */
        }
        main:function void(){
          z: string = foo("ABC");
          do{
            if(z=="ABCabc")
              while(true){
                //do nothing here
                while(true){
                  foo(foo(foo(foo("ASDASDASD"))));
                }
              }
            else for(i=1,i<=20,i+2){
              printInteger(i);
            }
            break;
          }while(true);
        }
      """
        expect = """Program([
	FuncDecl(foo, StringType, [OutParam(x, StringType)], None, BlockStmt([VarDecl(z, StringType, StringLit(abc)), ReturnStmt(BinExpr(::, Id(z), Id(x)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(z, StringType, FuncCall(foo, [StringLit(ABC)])), DoWhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(==, Id(z), StringLit(ABCabc)), WhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([CallStmt(foo, FuncCall(foo, [FuncCall(foo, [FuncCall(foo, [StringLit(ASDASDASD)])])]))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(20)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([CallStmt(printInteger, Id(i))]))), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_other4(self):
        input = r"""
        main:function void(){
      for (i = 1, i < 10, i + 1) {
        writeInt(i);
      }
        }
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_other5(self):
        input = r"""
        /* masdjaskd jklasjdk ljaklsjdlk jslkajdl jasd */
        ///
        ///////
        //sad asd/ as/d
        // 123 123
        main: function void(){}
      """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_more(self):
      input = """x: integer = 2_3_3 + 2323;"""
      expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, IntegerLit(233), IntegerLit(2323)))
])"""
      self.assertTrue(TestAST.test(input, expect, 391))

    def test_more2(self):
      input = """x: integer = 2_3_3 + 2323 -12 * 23 % 34;"""
      expect = """Program([
	VarDecl(x, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(233), IntegerLit(2323)), BinExpr(%, BinExpr(*, IntegerLit(12), IntegerLit(23)), IntegerLit(34))))
])"""
      self.assertTrue(TestAST.test(input, expect, 392))

    def test_more3(self):
      input = """x: integer = 2_3_3 + 2323;
      y: integer = 23;
      z: integer = x+y;"""
      expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, IntegerLit(233), IntegerLit(2323)))
	VarDecl(y, IntegerType, IntegerLit(23))
	VarDecl(z, IntegerType, BinExpr(+, Id(x), Id(y)))
])"""
      self.assertTrue(TestAST.test(input, expect, 393))

    def test_more4(self):
      input = """x: integer = 2_3_3 + 1_23_3 + 23;"""
      expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, BinExpr(+, IntegerLit(233), IntegerLit(1233)), IntegerLit(23)))
])"""
      self.assertTrue(TestAST.test(input, expect, 394))

    def test_func(self):
      input = """
      foo: function void() {}
      bar: function void() { foo();}
      """
      expect= """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([]))
	FuncDecl(bar, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
])"""
      self.assertTrue(TestAST.test(input, expect, 395))
    
    def test_func2(self):
      input = """
      foo: function void() {}
      bar: function void() { foo();}
      foobar: function void() {foo(); bar();}
      """
      expect= """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([]))
	FuncDecl(bar, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
	FuncDecl(foobar, VoidType, [], None, BlockStmt([CallStmt(foo, ), CallStmt(bar, )]))
])"""
      self.assertTrue(TestAST.test(input, expect, 396))
    
    def test_func3(self):
      input = """
      foobar: function void() {
        x: integer = 12;
        print(x);
      }
      """
      expect= """Program([
	FuncDecl(foobar, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(12)), CallStmt(print, Id(x))]))
])"""
      self.assertTrue(TestAST.test(input, expect, 397))

    def test_func4(self):
      input = """
      foobar: function void() {
        x: integer = 23;
        z: integer = 33;
        a: integer = x + z;
        print(a);
      }
      """
      expect= """Program([
	FuncDecl(foobar, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(23)), VarDecl(z, IntegerType, IntegerLit(33)), VarDecl(a, IntegerType, BinExpr(+, Id(x), Id(z))), CallStmt(print, Id(a))]))
])"""
      self.assertTrue(TestAST.test(input, expect, 398))

    def test_func5(self):
      input = """
      foobar: function void() {
        z: string = "HIIIII";
        print(z);
      }
      """
      expect= """Program([
	FuncDecl(foobar, VoidType, [], None, BlockStmt([VarDecl(z, StringType, StringLit(HIIIII)), CallStmt(print, Id(z))]))
])"""
      self.assertTrue(TestAST.test(input, expect, 399))