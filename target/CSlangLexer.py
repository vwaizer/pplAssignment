# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *;



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01c2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63\6\63")
        buf.write("\u013c\n\63\r\63\16\63\u013d\3\64\3\64\6\64\u0142\n\64")
        buf.write("\r\64\16\64\u0143\3\65\3\65\5\65\u0148\n\65\3\65\6\65")
        buf.write("\u014b\n\65\r\65\16\65\u014c\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u0159\n\66\3\67\3\67\5")
        buf.write("\67\u015d\n\67\38\38\38\38\38\39\39\39\39\39\39\3:\3:")
        buf.write("\7:\u016c\n:\f:\16:\u016f\13:\3;\3;\5;\u0173\n;\3<\3<")
        buf.write("\3<\3=\3=\3=\3=\7=\u017c\n=\f=\16=\u017f\13=\3=\7=\u0182")
        buf.write("\n=\f=\16=\u0185\13=\3=\3=\3=\3>\6>\u018b\n>\r>\16>\u018c")
        buf.write("\3>\3>\3?\3?\3?\3?\7?\u0195\n?\f?\16?\u0198\13?\3?\3?")
        buf.write("\3?\3?\3?\3@\3@\3@\3@\7@\u01a3\n@\f@\16@\u01a6\13@\3@")
        buf.write("\3@\3A\3A\3A\3B\6B\u01ae\nB\rB\16B\u01af\3C\3C\3C\3C\3")
        buf.write("D\3D\7D\u01b8\nD\fD\16D\u01bb\13D\3D\3D\3D\3E\3E\3E\3")
        buf.write("\u0196\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\2i\2k\65")
        buf.write("m\66o\67q8s9u\2w\2y:{;}<\177=\u0081\2\u0083>\u0085?\u0087")
        buf.write("@\u0089A\3\2\17\3\2^^\3\2\62;\3\2\60\60\4\2GGgg\4\2--")
        buf.write("//\3\2\63;\5\2\n\f\16\17^^\t\2))^^ddhhppttvv\3\2$$\5\2")
        buf.write("\13\f\17\17\"\"\4\2\f\f\17\17\b\2^^ddhhppttvv\6\2\62;")
        buf.write("C\\aac|\2\u01cd\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2")
        buf.write("\2\2s\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u0090\3\2\2\2\7\u0095")
        buf.write("\3\2\2\2\t\u00a0\3\2\2\2\13\u00a3\3\2\2\2\r\u00a8\3\2")
        buf.write("\2\2\17\u00ac\3\2\2\2\21\u00b5\3\2\2\2\23\u00bb\3\2\2")
        buf.write("\2\25\u00c2\3\2\2\2\27\u00c7\3\2\2\2\31\u00cc\3\2\2\2")
        buf.write("\33\u00d0\3\2\2\2\35\u00d6\3\2\2\2\37\u00da\3\2\2\2!\u00e0")
        buf.write("\3\2\2\2#\u00e2\3\2\2\2%\u00e4\3\2\2\2\'\u00e6\3\2\2\2")
        buf.write(")\u00e8\3\2\2\2+\u00eb\3\2\2\2-\u00ed\3\2\2\2/\u00ef\3")
        buf.write("\2\2\2\61\u00f3\3\2\2\2\63\u00f9\3\2\2\2\65\u00fb\3\2")
        buf.write("\2\2\67\u00fd\3\2\2\29\u00ff\3\2\2\2;\u0101\3\2\2\2=\u0103")
        buf.write("\3\2\2\2?\u0105\3\2\2\2A\u0108\3\2\2\2C\u010b\3\2\2\2")
        buf.write("E\u010d\3\2\2\2G\u010f\3\2\2\2I\u0112\3\2\2\2K\u0115\3")
        buf.write("\2\2\2M\u0118\3\2\2\2O\u011b\3\2\2\2Q\u011d\3\2\2\2S\u011f")
        buf.write("\3\2\2\2U\u0121\3\2\2\2W\u0123\3\2\2\2Y\u0125\3\2\2\2")
        buf.write("[\u0127\3\2\2\2]\u0129\3\2\2\2_\u012e\3\2\2\2a\u0130\3")
        buf.write("\2\2\2c\u0137\3\2\2\2e\u013b\3\2\2\2g\u013f\3\2\2\2i\u0145")
        buf.write("\3\2\2\2k\u0158\3\2\2\2m\u015c\3\2\2\2o\u015e\3\2\2\2")
        buf.write("q\u0163\3\2\2\2s\u0169\3\2\2\2u\u0172\3\2\2\2w\u0174\3")
        buf.write("\2\2\2y\u0177\3\2\2\2{\u018a\3\2\2\2}\u0190\3\2\2\2\177")
        buf.write("\u019e\3\2\2\2\u0081\u01a9\3\2\2\2\u0083\u01ad\3\2\2\2")
        buf.write("\u0085\u01b1\3\2\2\2\u0087\u01b5\3\2\2\2\u0089\u01bf\3")
        buf.write("\2\2\2\u008b\u008c\7p\2\2\u008c\u008d\7w\2\2\u008d\u008e")
        buf.write("\7n\2\2\u008e\u008f\7n\2\2\u008f\4\3\2\2\2\u0090\u0091")
        buf.write("\7u\2\2\u0091\u0092\7g\2\2\u0092\u0093\7n\2\2\u0093\u0094")
        buf.write("\7h\2\2\u0094\6\3\2\2\2\u0095\u0096\7e\2\2\u0096\u0097")
        buf.write("\7q\2\2\u0097\u0098\7p\2\2\u0098\u0099\7v\2\2\u0099\u009a")
        buf.write("\7t\2\2\u009a\u009b\7w\2\2\u009b\u009c\7e\2\2\u009c\u009d")
        buf.write("\7v\2\2\u009d\u009e\7q\2\2\u009e\u009f\7t\2\2\u009f\b")
        buf.write("\3\2\2\2\u00a0\u00a1\7k\2\2\u00a1\u00a2\7h\2\2\u00a2\n")
        buf.write("\3\2\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\7n\2\2\u00a5\u00a6")
        buf.write("\7u\2\2\u00a6\u00a7\7g\2\2\u00a7\f\3\2\2\2\u00a8\u00a9")
        buf.write("\7h\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7t\2\2\u00ab\16")
        buf.write("\3\2\2\2\u00ac\u00ad\7e\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7w\2\2\u00b3\u00b4\7g\2\2\u00b4\20")
        buf.write("\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7m\2\2\u00ba\22")
        buf.write("\3\2\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7p\2\2\u00c1\24\3\2\2\2\u00c2\u00c3\7x\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7f\2\2\u00c6\26")
        buf.write("\3\2\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7e\2\2\u00cb\30\3\2\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7y\2\2\u00cf\32")
        buf.write("\3\2\2\2\u00d0\u00d1\7e\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7u\2\2\u00d4\u00d5\7v\2\2\u00d5\34")
        buf.write("\3\2\2\2\u00d6\u00d7\7x\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\36\3\2\2\2\u00da\u00db\7e\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de\7u\2\2\u00de\u00df")
        buf.write("\7u\2\2\u00df \3\2\2\2\u00e0\u00e1\7}\2\2\u00e1\"\3\2")
        buf.write("\2\2\u00e2\u00e3\7\177\2\2\u00e3$\3\2\2\2\u00e4\u00e5")
        buf.write("\7=\2\2\u00e5&\3\2\2\2\u00e6\u00e7\7<\2\2\u00e7(\3\2\2")
        buf.write("\2\u00e8\u00e9\7>\2\2\u00e9\u00ea\7/\2\2\u00ea*\3\2\2")
        buf.write("\2\u00eb\u00ec\7?\2\2\u00ec,\3\2\2\2\u00ed\u00ee\7.\2")
        buf.write("\2\u00ee.\3\2\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2")
        buf.write("\2\u00f1\u00f2\7v\2\2\u00f2\60\3\2\2\2\u00f3\u00f4\7h")
        buf.write("\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7")
        buf.write("\7c\2\2\u00f7\u00f8\7v\2\2\u00f8\62\3\2\2\2\u00f9\u00fa")
        buf.write("\7B\2\2\u00fa\64\3\2\2\2\u00fb\u00fc\7+\2\2\u00fc\66\3")
        buf.write("\2\2\2\u00fd\u00fe\7*\2\2\u00fe8\3\2\2\2\u00ff\u0100\7")
        buf.write("]\2\2\u0100:\3\2\2\2\u0101\u0102\7_\2\2\u0102<\3\2\2\2")
        buf.write("\u0103\u0104\7`\2\2\u0104>\3\2\2\2\u0105\u0106\7?\2\2")
        buf.write("\u0106\u0107\7?\2\2\u0107@\3\2\2\2\u0108\u0109\7#\2\2")
        buf.write("\u0109\u010a\7?\2\2\u010aB\3\2\2\2\u010b\u010c\7>\2\2")
        buf.write("\u010cD\3\2\2\2\u010d\u010e\7@\2\2\u010eF\3\2\2\2\u010f")
        buf.write("\u0110\7>\2\2\u0110\u0111\7?\2\2\u0111H\3\2\2\2\u0112")
        buf.write("\u0113\7@\2\2\u0113\u0114\7?\2\2\u0114J\3\2\2\2\u0115")
        buf.write("\u0116\7(\2\2\u0116\u0117\7(\2\2\u0117L\3\2\2\2\u0118")
        buf.write("\u0119\7~\2\2\u0119\u011a\7~\2\2\u011aN\3\2\2\2\u011b")
        buf.write("\u011c\7-\2\2\u011cP\3\2\2\2\u011d\u011e\7/\2\2\u011e")
        buf.write("R\3\2\2\2\u011f\u0120\7,\2\2\u0120T\3\2\2\2\u0121\u0122")
        buf.write("\7\61\2\2\u0122V\3\2\2\2\u0123\u0124\7#\2\2\u0124X\3\2")
        buf.write("\2\2\u0125\u0126\t\2\2\2\u0126Z\3\2\2\2\u0127\u0128\7")
        buf.write("\'\2\2\u0128\\\3\2\2\2\u0129\u012a\7d\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\u012c\7q\2\2\u012c\u012d\7n\2\2\u012d^\3")
        buf.write("\2\2\2\u012e\u012f\7\60\2\2\u012f`\3\2\2\2\u0130\u0131")
        buf.write("\7u\2\2\u0131\u0132\7v\2\2\u0132\u0133\7t\2\2\u0133\u0134")
        buf.write("\7k\2\2\u0134\u0135\7p\2\2\u0135\u0136\7i\2\2\u0136b\3")
        buf.write("\2\2\2\u0137\u0138\7<\2\2\u0138\u0139\7?\2\2\u0139d\3")
        buf.write("\2\2\2\u013a\u013c\t\3\2\2\u013b\u013a\3\2\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("f\3\2\2\2\u013f\u0141\t\4\2\2\u0140\u0142\t\3\2\2\u0141")
        buf.write("\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144h\3\2\2\2\u0145\u0147\t\5\2")
        buf.write("\2\u0146\u0148\t\6\2\2\u0147\u0146\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u014a\3\2\2\2\u0149\u014b\t\3\2\2\u014a")
        buf.write("\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2\2\2")
        buf.write("\u014c\u014d\3\2\2\2\u014dj\3\2\2\2\u014e\u014f\5e\63")
        buf.write("\2\u014f\u0150\5g\64\2\u0150\u0151\5i\65\2\u0151\u0159")
        buf.write("\3\2\2\2\u0152\u0153\5e\63\2\u0153\u0154\5i\65\2\u0154")
        buf.write("\u0159\3\2\2\2\u0155\u0156\5e\63\2\u0156\u0157\5g\64\2")
        buf.write("\u0157\u0159\3\2\2\2\u0158\u014e\3\2\2\2\u0158\u0152\3")
        buf.write("\2\2\2\u0158\u0155\3\2\2\2\u0159l\3\2\2\2\u015a\u015d")
        buf.write("\5o8\2\u015b\u015d\5q9\2\u015c\u015a\3\2\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015dn\3\2\2\2\u015e\u015f\7v\2\2\u015f\u0160")
        buf.write("\7t\2\2\u0160\u0161\7w\2\2\u0161\u0162\7g\2\2\u0162p\3")
        buf.write("\2\2\2\u0163\u0164\7h\2\2\u0164\u0165\7c\2\2\u0165\u0166")
        buf.write("\7n\2\2\u0166\u0167\7u\2\2\u0167\u0168\7g\2\2\u0168r\3")
        buf.write("\2\2\2\u0169\u016d\t\7\2\2\u016a\u016c\t\3\2\2\u016b\u016a")
        buf.write("\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016et\3\2\2\2\u016f\u016d\3\2\2\2\u0170")
        buf.write("\u0173\n\b\2\2\u0171\u0173\7^\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0172\u0171\3\2\2\2\u0173v\3\2\2\2\u0174\u0175\7^\2\2")
        buf.write("\u0175\u0176\t\t\2\2\u0176x\3\2\2\2\u0177\u0183\7$\2\2")
        buf.write("\u0178\u0182\5u;\2\u0179\u017d\t\n\2\2\u017a\u017c\5u")
        buf.write(";\2\u017b\u017a\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u0180\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0182\t\n\2\2\u0181\u0178\3\2\2\2")
        buf.write("\u0181\u0179\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3")
        buf.write("\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0186\u0187\7$\2\2\u0187\u0188\b=\2\2\u0188z")
        buf.write("\3\2\2\2\u0189\u018b\t\13\2\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018e\u018f\b>\3\2\u018f|\3\2\2\2")
        buf.write("\u0190\u0191\7\61\2\2\u0191\u0192\7,\2\2\u0192\u0196\3")
        buf.write("\2\2\2\u0193\u0195\13\2\2\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u0198\3\2\2\2\u0196\u0197\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0197\u0199\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\7")
        buf.write(",\2\2\u019a\u019b\7\61\2\2\u019b\u019c\3\2\2\2\u019c\u019d")
        buf.write("\b?\3\2\u019d~\3\2\2\2\u019e\u019f\7\61\2\2\u019f\u01a0")
        buf.write("\7\61\2\2\u01a0\u01a4\3\2\2\2\u01a1\u01a3\n\f\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u01a4\3")
        buf.write("\2\2\2\u01a7\u01a8\b@\3\2\u01a8\u0080\3\2\2\2\u01a9\u01aa")
        buf.write("\7^\2\2\u01aa\u01ab\t\r\2\2\u01ab\u0082\3\2\2\2\u01ac")
        buf.write("\u01ae\t\16\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2")
        buf.write("\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u0084")
        buf.write("\3\2\2\2\u01b1\u01b2\7$\2\2\u01b2\u01b3\7\2\2\3\u01b3")
        buf.write("\u01b4\bC\4\2\u01b4\u0086\3\2\2\2\u01b5\u01b9\7$\2\2\u01b6")
        buf.write("\u01b8\5u;\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9")
        buf.write("\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc\3\2\2\2")
        buf.write("\u01bb\u01b9\3\2\2\2\u01bc\u01bd\5\u0081A\2\u01bd\u01be")
        buf.write("\bD\5\2\u01be\u0088\3\2\2\2\u01bf\u01c0\13\2\2\2\u01c0")
        buf.write("\u01c1\bE\6\2\u01c1\u008a\3\2\2\2\23\2\u013d\u0143\u0147")
        buf.write("\u014c\u0158\u015c\u016d\u0172\u017d\u0181\u0183\u018c")
        buf.write("\u0196\u01a4\u01af\u01b9\7\3=\2\b\2\2\3C\3\3D\4\3E\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NULL = 1
    SELF = 2
    CONTRUCTOR = 3
    IF = 4
    ELSE = 5
    FOR = 6
    CONTINUE = 7
    BREAK = 8
    RETURN = 9
    VOID = 10
    FUNCTION = 11
    NEW = 12
    CONST = 13
    VAR = 14
    CLASS = 15
    LCB = 16
    RCB = 17
    SEMI = 18
    COLON = 19
    RARROW = 20
    EQUAL = 21
    COMMA = 22
    INT = 23
    FLOAT = 24
    SIGN = 25
    RB = 26
    LB = 27
    LSB = 28
    RSB = 29
    STRING_OP = 30
    EQ_OP = 31
    NEQ_OP = 32
    LT_OP = 33
    GT_OP = 34
    LEQ_OP = 35
    GEQ_OP = 36
    AND_OP = 37
    OR_OP = 38
    ADD_OP = 39
    SUB_OP = 40
    MUL_OP = 41
    F_DIV_OP = 42
    NOT_OP = 43
    I_DIV_OP = 44
    REM_OP = 45
    BOOL = 46
    DOT = 47
    STRING = 48
    ASSGIN_OP = 49
    INTLIT = 50
    FLOATLIT = 51
    BOOLLIT = 52
    TRUE = 53
    FALSE = 54
    DIM = 55
    STRINGLIT = 56
    WS = 57
    C_COMMENT = 58
    CPP_COMMENT = 59
    ID = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'null'", "'self'", "'contructor'", "'if'", "'else'", "'for'", 
            "'continue'", "'break'", "'return'", "'void'", "'func'", "'new'", 
            "'const'", "'var'", "'class'", "'{'", "'}'", "';'", "':'", "'<-'", 
            "'='", "','", "'int'", "'float'", "'@'", "')'", "'('", "'['", 
            "']'", "'^'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'&&'", "'||'", "'+'", "'-'", "'*'", "'/'", "'!'", "'%'", "'bool'", 
            "'.'", "'string'", "':='", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "NULL", "SELF", "CONTRUCTOR", "IF", "ELSE", "FOR", "CONTINUE", 
            "BREAK", "RETURN", "VOID", "FUNCTION", "NEW", "CONST", "VAR", 
            "CLASS", "LCB", "RCB", "SEMI", "COLON", "RARROW", "EQUAL", "COMMA", 
            "INT", "FLOAT", "SIGN", "RB", "LB", "LSB", "RSB", "STRING_OP", 
            "EQ_OP", "NEQ_OP", "LT_OP", "GT_OP", "LEQ_OP", "GEQ_OP", "AND_OP", 
            "OR_OP", "ADD_OP", "SUB_OP", "MUL_OP", "F_DIV_OP", "NOT_OP", 
            "I_DIV_OP", "REM_OP", "BOOL", "DOT", "STRING", "ASSGIN_OP", 
            "INTLIT", "FLOATLIT", "BOOLLIT", "TRUE", "FALSE", "DIM", "STRINGLIT", 
            "WS", "C_COMMENT", "CPP_COMMENT", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "NULL", "SELF", "CONTRUCTOR", "IF", "ELSE", "FOR", "CONTINUE", 
                  "BREAK", "RETURN", "VOID", "FUNCTION", "NEW", "CONST", 
                  "VAR", "CLASS", "LCB", "RCB", "SEMI", "COLON", "RARROW", 
                  "EQUAL", "COMMA", "INT", "FLOAT", "SIGN", "RB", "LB", 
                  "LSB", "RSB", "STRING_OP", "EQ_OP", "NEQ_OP", "LT_OP", 
                  "GT_OP", "LEQ_OP", "GEQ_OP", "AND_OP", "OR_OP", "ADD_OP", 
                  "SUB_OP", "MUL_OP", "F_DIV_OP", "NOT_OP", "I_DIV_OP", 
                  "REM_OP", "BOOL", "DOT", "STRING", "ASSGIN_OP", "INTLIT", 
                  "DecimalPart", "ExponentPart", "FLOATLIT", "BOOLLIT", 
                  "TRUE", "FALSE", "DIM", "STR_CHAR", "ESC_SEQ", "STRINGLIT", 
                  "WS", "C_COMMENT", "CPP_COMMENT", "ESC_ILLEGAL", "ID", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.STRINGLIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise IllegalEscape(self.text[1:] )
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text) 
     


