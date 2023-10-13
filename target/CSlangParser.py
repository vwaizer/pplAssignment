# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01f0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\6\2\u0082\n\2\r\2")
        buf.write("\16\2\u0083\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008e")
        buf.write("\n\3\3\3\3\3\7\3\u0092\n\3\f\3\16\3\u0095\13\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\5\4\u009c\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\5\7\u00a9\n\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00b6\n\t\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00c6")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00cd\n\f\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00d6\n\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00dd\n\17\3\20\3\20\3\20\3\20\3\20\3\20\7")
        buf.write("\20\u00e5\n\20\f\20\16\20\u00e8\13\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\7\21\u00f0\n\21\f\21\16\21\u00f3\13\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\7\22\u00fb\n\22\f\22\16\22")
        buf.write("\u00fe\13\22\3\23\3\23\3\23\5\23\u0103\n\23\3\24\3\24")
        buf.write("\3\24\5\24\u0108\n\24\3\25\3\25\3\25\3\25\5\25\u010e\n")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0116\n\26\f\26")
        buf.write("\16\26\u0119\13\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u0121\n\27\3\30\3\30\3\30\3\30\5\30\u0127\n\30\3\31\3")
        buf.write("\31\5\31\u012b\n\31\3\32\3\32\3\32\3\33\3\33\5\33\u0132")
        buf.write("\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u013d\n\34\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37\5")
        buf.write("\37\u0147\n\37\3 \3 \3 \3 \3 \5 \u014e\n \3!\3!\5!\u0152")
        buf.write("\n!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\5$\u0160\n")
        buf.write("$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\5&\u016f\n&\3")
        buf.write("\'\3\'\5\'\u0173\n\'\3\'\3\'\3(\3(\3(\3(\3(\5(\u017c\n")
        buf.write("(\3)\3)\3)\3)\3*\3*\3+\3+\3+\5+\u0187\n+\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\5,\u0190\n,\3,\3,\3,\3-\3-\5-\u0197\n-\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\5.\u01a0\n.\3/\3/\5/\u01a4\n/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\5\62\u01ae\n\62\3\62\3")
        buf.write("\62\3\63\3\63\5\63\u01b4\n\63\3\63\3\63\3\64\6\64\u01b9")
        buf.write("\n\64\r\64\16\64\u01ba\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\5\65\u01c6\n\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\38\38\58\u01d1\n8\39\39\3:\3:\5:\u01d7\n:\3")
        buf.write(":\3:\3:\5:\u01dc\n:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\3@\2\6\36 \"*A\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\2\6\3\2\'(\3\2)*\4\2+,./\3\2!")
        buf.write("&\2\u01e9\2\u0081\3\2\2\2\4\u0087\3\2\2\2\6\u009b\3\2")
        buf.write("\2\2\b\u009d\3\2\2\2\n\u00a1\3\2\2\2\f\u00a5\3\2\2\2\16")
        buf.write("\u00ac\3\2\2\2\20\u00b5\3\2\2\2\22\u00b7\3\2\2\2\24\u00c5")
        buf.write("\3\2\2\2\26\u00cc\3\2\2\2\30\u00ce\3\2\2\2\32\u00d5\3")
        buf.write("\2\2\2\34\u00dc\3\2\2\2\36\u00de\3\2\2\2 \u00e9\3\2\2")
        buf.write("\2\"\u00f4\3\2\2\2$\u0102\3\2\2\2&\u0107\3\2\2\2(\u010d")
        buf.write("\3\2\2\2*\u010f\3\2\2\2,\u0120\3\2\2\2.\u0126\3\2\2\2")
        buf.write("\60\u012a\3\2\2\2\62\u012c\3\2\2\2\64\u012f\3\2\2\2\66")
        buf.write("\u013c\3\2\2\28\u013e\3\2\2\2:\u0142\3\2\2\2<\u0146\3")
        buf.write("\2\2\2>\u014d\3\2\2\2@\u0151\3\2\2\2B\u0153\3\2\2\2D\u0156")
        buf.write("\3\2\2\2F\u015b\3\2\2\2H\u0163\3\2\2\2J\u016e\3\2\2\2")
        buf.write("L\u0170\3\2\2\2N\u017b\3\2\2\2P\u017d\3\2\2\2R\u0181\3")
        buf.write("\2\2\2T\u0186\3\2\2\2V\u018f\3\2\2\2X\u0194\3\2\2\2Z\u019f")
        buf.write("\3\2\2\2\\\u01a3\3\2\2\2^\u01a5\3\2\2\2`\u01a8\3\2\2\2")
        buf.write("b\u01ab\3\2\2\2d\u01b1\3\2\2\2f\u01b8\3\2\2\2h\u01c5\3")
        buf.write("\2\2\2j\u01c7\3\2\2\2l\u01ca\3\2\2\2n\u01d0\3\2\2\2p\u01d2")
        buf.write("\3\2\2\2r\u01d4\3\2\2\2t\u01dd\3\2\2\2v\u01df\3\2\2\2")
        buf.write("x\u01e1\3\2\2\2z\u01e3\3\2\2\2|\u01e6\3\2\2\2~\u01ed\3")
        buf.write("\2\2\2\u0080\u0082\5\4\3\2\u0081\u0080\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0086\7\2\2\3\u0086\3\3\2\2\2\u0087")
        buf.write("\u008d\7\21\2\2\u0088\u008e\5@!\2\u0089\u008a\5@!\2\u008a")
        buf.write("\u008b\7\26\2\2\u008b\u008c\5@!\2\u008c\u008e\3\2\2\2")
        buf.write("\u008d\u0088\3\2\2\2\u008d\u0089\3\2\2\2\u008e\u008f\3")
        buf.write("\2\2\2\u008f\u0093\7\22\2\2\u0090\u0092\5\6\4\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093\3")
        buf.write("\2\2\2\u0096\u0097\7\23\2\2\u0097\5\3\2\2\2\u0098\u009c")
        buf.write("\5\f\7\2\u0099\u009c\5H%\2\u009a\u009c\5\b\5\2\u009b\u0098")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\7\3\2\2\2\u009d\u009e\7\17\2\2\u009e\u009f\5\n\6\2\u009f")
        buf.write("\u00a0\7\24\2\2\u00a0\t\3\2\2\2\u00a1\u00a2\5@!\2\u00a2")
        buf.write("\u00a3\5\24\13\2\u00a3\u00a4\5\30\r\2\u00a4\13\3\2\2\2")
        buf.write("\u00a5\u00a8\7\20\2\2\u00a6\u00a9\5\16\b\2\u00a7\u00a9")
        buf.write("\5\22\n\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00ab\7\24\2\2\u00ab\r\3\2\2\2\u00ac")
        buf.write("\u00ad\5\20\t\2\u00ad\u00ae\7\25\2\2\u00ae\u00af\5<\37")
        buf.write("\2\u00af\17\3\2\2\2\u00b0\u00b1\5@!\2\u00b1\u00b2\7\30")
        buf.write("\2\2\u00b2\u00b3\5\20\t\2\u00b3\u00b6\3\2\2\2\u00b4\u00b6")
        buf.write("\5@!\2\u00b5\u00b0\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\21")
        buf.write("\3\2\2\2\u00b7\u00b8\5@!\2\u00b8\u00b9\5\24\13\2\u00b9")
        buf.write("\u00ba\5\30\r\2\u00ba\23\3\2\2\2\u00bb\u00bc\7\30\2\2")
        buf.write("\u00bc\u00bd\5@!\2\u00bd\u00be\5\24\13\2\u00be\u00bf\5")
        buf.write("\30\r\2\u00bf\u00c0\7\30\2\2\u00c0\u00c6\3\2\2\2\u00c1")
        buf.write("\u00c2\7\25\2\2\u00c2\u00c3\5<\37\2\u00c3\u00c4\7\27\2")
        buf.write("\2\u00c4\u00c6\3\2\2\2\u00c5\u00bb\3\2\2\2\u00c5\u00c1")
        buf.write("\3\2\2\2\u00c6\25\3\2\2\2\u00c7\u00c8\5\30\r\2\u00c8\u00c9")
        buf.write("\7\30\2\2\u00c9\u00ca\5\26\f\2\u00ca\u00cd\3\2\2\2\u00cb")
        buf.write("\u00cd\5\30\r\2\u00cc\u00c7\3\2\2\2\u00cc\u00cb\3\2\2")
        buf.write("\2\u00cd\27\3\2\2\2\u00ce\u00cf\5\32\16\2\u00cf\31\3\2")
        buf.write("\2\2\u00d0\u00d1\5\34\17\2\u00d1\u00d2\7 \2\2\u00d2\u00d3")
        buf.write("\5\34\17\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6\5\34\17\2\u00d5")
        buf.write("\u00d0\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\33\3\2\2\2\u00d7")
        buf.write("\u00d8\5\36\20\2\u00d8\u00d9\5:\36\2\u00d9\u00da\5\36")
        buf.write("\20\2\u00da\u00dd\3\2\2\2\u00db\u00dd\5\36\20\2\u00dc")
        buf.write("\u00d7\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\35\3\2\2\2\u00de")
        buf.write("\u00df\b\20\1\2\u00df\u00e0\5 \21\2\u00e0\u00e6\3\2\2")
        buf.write("\2\u00e1\u00e2\f\4\2\2\u00e2\u00e3\t\2\2\2\u00e3\u00e5")
        buf.write("\5 \21\2\u00e4\u00e1\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\37\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e9\u00ea\b\21\1\2\u00ea\u00eb\5\"\22")
        buf.write("\2\u00eb\u00f1\3\2\2\2\u00ec\u00ed\f\4\2\2\u00ed\u00ee")
        buf.write("\t\3\2\2\u00ee\u00f0\5\"\22\2\u00ef\u00ec\3\2\2\2\u00f0")
        buf.write("\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2!\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\b\22\1")
        buf.write("\2\u00f5\u00f6\5$\23\2\u00f6\u00fc\3\2\2\2\u00f7\u00f8")
        buf.write("\f\4\2\2\u00f8\u00f9\t\4\2\2\u00f9\u00fb\5$\23\2\u00fa")
        buf.write("\u00f7\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd#\3\2\2\2\u00fe\u00fc\3\2\2")
        buf.write("\2\u00ff\u0100\7-\2\2\u0100\u0103\5$\23\2\u0101\u0103")
        buf.write("\5&\24\2\u0102\u00ff\3\2\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("%\3\2\2\2\u0104\u0105\7*\2\2\u0105\u0108\5&\24\2\u0106")
        buf.write("\u0108\5(\25\2\u0107\u0104\3\2\2\2\u0107\u0106\3\2\2\2")
        buf.write("\u0108\'\3\2\2\2\u0109\u010a\5*\26\2\u010a\u010b\5\64")
        buf.write("\33\2\u010b\u010e\3\2\2\2\u010c\u010e\5*\26\2\u010d\u0109")
        buf.write("\3\2\2\2\u010d\u010c\3\2\2\2\u010e)\3\2\2\2\u010f\u0110")
        buf.write("\b\26\1\2\u0110\u0111\5,\27\2\u0111\u0117\3\2\2\2\u0112")
        buf.write("\u0113\f\4\2\2\u0113\u0114\7\61\2\2\u0114\u0116\5,\27")
        buf.write("\2\u0115\u0112\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118+\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u011a\u011b\5.\30\2\u011b\u011c\7\61\2\2\u011c")
        buf.write("\u011d\7\33\2\2\u011d\u011e\5.\30\2\u011e\u0121\3\2\2")
        buf.write("\2\u011f\u0121\5.\30\2\u0120\u011a\3\2\2\2\u0120\u011f")
        buf.write("\3\2\2\2\u0121-\3\2\2\2\u0122\u0123\5F$\2\u0123\u0124")
        buf.write("\5.\30\2\u0124\u0127\3\2\2\2\u0125\u0127\5\60\31\2\u0126")
        buf.write("\u0122\3\2\2\2\u0126\u0125\3\2\2\2\u0127/\3\2\2\2\u0128")
        buf.write("\u012b\5\62\32\2\u0129\u012b\5\66\34\2\u012a\u0128\3\2")
        buf.write("\2\2\u012a\u0129\3\2\2\2\u012b\61\3\2\2\2\u012c\u012d")
        buf.write("\5@!\2\u012d\u012e\5\64\33\2\u012e\63\3\2\2\2\u012f\u0131")
        buf.write("\7\36\2\2\u0130\u0132\5\26\f\2\u0131\u0130\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\7\37\2")
        buf.write("\2\u0134\65\3\2\2\2\u0135\u013d\7\64\2\2\u0136\u013d\7")
        buf.write("\65\2\2\u0137\u013d\7\66\2\2\u0138\u013d\7:\2\2\u0139")
        buf.write("\u013d\5V,\2\u013a\u013d\5@!\2\u013b\u013d\58\35\2\u013c")
        buf.write("\u0135\3\2\2\2\u013c\u0136\3\2\2\2\u013c\u0137\3\2\2\2")
        buf.write("\u013c\u0138\3\2\2\2\u013c\u0139\3\2\2\2\u013c\u013a\3")
        buf.write("\2\2\2\u013c\u013b\3\2\2\2\u013d\67\3\2\2\2\u013e\u013f")
        buf.write("\7\35\2\2\u013f\u0140\5\30\r\2\u0140\u0141\7\34\2\2\u0141")
        buf.write("9\3\2\2\2\u0142\u0143\t\5\2\2\u0143;\3\2\2\2\u0144\u0147")
        buf.write("\5> \2\u0145\u0147\5D#\2\u0146\u0144\3\2\2\2\u0146\u0145")
        buf.write("\3\2\2\2\u0147=\3\2\2\2\u0148\u014e\7\31\2\2\u0149\u014e")
        buf.write("\7\32\2\2\u014a\u014e\7\60\2\2\u014b\u014e\7\62\2\2\u014c")
        buf.write("\u014e\5D#\2\u014d\u0148\3\2\2\2\u014d\u0149\3\2\2\2\u014d")
        buf.write("\u014a\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e?\3\2\2\2\u014f\u0152\7>\2\2\u0150\u0152\5B\"\2")
        buf.write("\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152A\3\2\2")
        buf.write("\2\u0153\u0154\7\33\2\2\u0154\u0155\7>\2\2\u0155C\3\2")
        buf.write("\2\2\u0156\u0157\7\22\2\2\u0157\u0158\79\2\2\u0158\u0159")
        buf.write("\7\23\2\2\u0159\u015a\5> \2\u015aE\3\2\2\2\u015b\u015c")
        buf.write("\7\16\2\2\u015c\u015d\5<\37\2\u015d\u015f\7\35\2\2\u015e")
        buf.write("\u0160\5\26\f\2\u015f\u015e\3\2\2\2\u015f\u0160\3\2\2")
        buf.write("\2\u0160\u0161\3\2\2\2\u0161\u0162\7\34\2\2\u0162G\3\2")
        buf.write("\2\2\u0163\u0164\7\r\2\2\u0164\u0165\5J&\2\u0165\u0166")
        buf.write("\5R*\2\u0166I\3\2\2\2\u0167\u0168\5@!\2\u0168\u0169\5")
        buf.write("L\'\2\u0169\u016a\7\25\2\2\u016a\u016b\5\\/\2\u016b\u016f")
        buf.write("\3\2\2\2\u016c\u016d\7\5\2\2\u016d\u016f\5L\'\2\u016e")
        buf.write("\u0167\3\2\2\2\u016e\u016c\3\2\2\2\u016fK\3\2\2\2\u0170")
        buf.write("\u0172\7\35\2\2\u0171\u0173\5N(\2\u0172\u0171\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\7")
        buf.write("\34\2\2\u0175M\3\2\2\2\u0176\u0177\5P)\2\u0177\u0178\7")
        buf.write("\30\2\2\u0178\u0179\5N(\2\u0179\u017c\3\2\2\2\u017a\u017c")
        buf.write("\5P)\2\u017b\u0176\3\2\2\2\u017b\u017a\3\2\2\2\u017cO")
        buf.write("\3\2\2\2\u017d\u017e\5@!\2\u017e\u017f\7\25\2\2\u017f")
        buf.write("\u0180\5<\37\2\u0180Q\3\2\2\2\u0181\u0182\5d\63\2\u0182")
        buf.write("S\3\2\2\2\u0183\u0184\5@!\2\u0184\u0185\7\61\2\2\u0185")
        buf.write("\u0187\3\2\2\2\u0186\u0183\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188\u0189\5@!\2\u0189\u018a\5X")
        buf.write("-\2\u018a\u018b\7\24\2\2\u018bU\3\2\2\2\u018c\u018d\5")
        buf.write("@!\2\u018d\u018e\7\61\2\2\u018e\u0190\3\2\2\2\u018f\u018c")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("\u0192\5@!\2\u0192\u0193\5X-\2\u0193W\3\2\2\2\u0194\u0196")
        buf.write("\7\35\2\2\u0195\u0197\5Z.\2\u0196\u0195\3\2\2\2\u0196")
        buf.write("\u0197\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\7\34\2")
        buf.write("\2\u0199Y\3\2\2\2\u019a\u019b\5\30\r\2\u019b\u019c\7\30")
        buf.write("\2\2\u019c\u019d\5Z.\2\u019d\u01a0\3\2\2\2\u019e\u01a0")
        buf.write("\5\30\r\2\u019f\u019a\3\2\2\2\u019f\u019e\3\2\2\2\u01a0")
        buf.write("[\3\2\2\2\u01a1\u01a4\7\f\2\2\u01a2\u01a4\5> \2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4]\3\2\2\2\u01a5")
        buf.write("\u01a6\7\t\2\2\u01a6\u01a7\7\24\2\2\u01a7_\3\2\2\2\u01a8")
        buf.write("\u01a9\7\n\2\2\u01a9\u01aa\7\24\2\2\u01aaa\3\2\2\2\u01ab")
        buf.write("\u01ad\7\13\2\2\u01ac\u01ae\5\30\r\2\u01ad\u01ac\3\2\2")
        buf.write("\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0")
        buf.write("\7\24\2\2\u01b0c\3\2\2\2\u01b1\u01b3\7\22\2\2\u01b2\u01b4")
        buf.write("\5f\64\2\u01b3\u01b2\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b6\7\23\2\2\u01b6e\3\2\2\2\u01b7")
        buf.write("\u01b9\5h\65\2\u01b8\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2")
        buf.write("\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bbg\3\2\2")
        buf.write("\2\u01bc\u01c6\5j\66\2\u01bd\u01c6\5r:\2\u01be\u01c6\5")
        buf.write("|?\2\u01bf\u01c6\5b\62\2\u01c0\u01c6\5`\61\2\u01c1\u01c6")
        buf.write("\5^\60\2\u01c2\u01c6\5d\63\2\u01c3\u01c6\5\f\7\2\u01c4")
        buf.write("\u01c6\5T+\2\u01c5\u01bc\3\2\2\2\u01c5\u01bd\3\2\2\2\u01c5")
        buf.write("\u01be\3\2\2\2\u01c5\u01bf\3\2\2\2\u01c5\u01c0\3\2\2\2")
        buf.write("\u01c5\u01c1\3\2\2\2\u01c5\u01c2\3\2\2\2\u01c5\u01c3\3")
        buf.write("\2\2\2\u01c5\u01c4\3\2\2\2\u01c6i\3\2\2\2\u01c7\u01c8")
        buf.write("\5l\67\2\u01c8\u01c9\7\24\2\2\u01c9k\3\2\2\2\u01ca\u01cb")
        buf.write("\5n8\2\u01cb\u01cc\7\63\2\2\u01cc\u01cd\5p9\2\u01cdm\3")
        buf.write("\2\2\2\u01ce\u01d1\5@!\2\u01cf\u01d1\5\62\32\2\u01d0\u01ce")
        buf.write("\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1o\3\2\2\2\u01d2\u01d3")
        buf.write("\5\30\r\2\u01d3q\3\2\2\2\u01d4\u01d6\7\6\2\2\u01d5\u01d7")
        buf.write("\5t;\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01d9\5v<\2\u01d9\u01db\5x=\2\u01da\u01dc")
        buf.write("\5z>\2\u01db\u01da\3\2\2\2\u01db\u01dc\3\2\2\2\u01dcs")
        buf.write("\3\2\2\2\u01dd\u01de\5d\63\2\u01deu\3\2\2\2\u01df\u01e0")
        buf.write("\5\30\r\2\u01e0w\3\2\2\2\u01e1\u01e2\5d\63\2\u01e2y\3")
        buf.write("\2\2\2\u01e3\u01e4\7\7\2\2\u01e4\u01e5\5d\63\2\u01e5{")
        buf.write("\3\2\2\2\u01e6\u01e7\7\b\2\2\u01e7\u01e8\5j\66\2\u01e8")
        buf.write("\u01e9\5\30\r\2\u01e9\u01ea\7\24\2\2\u01ea\u01eb\5j\66")
        buf.write("\2\u01eb\u01ec\5~@\2\u01ec}\3\2\2\2\u01ed\u01ee\5d\63")
        buf.write("\2\u01ee\177\3\2\2\2+\u0083\u008d\u0093\u009b\u00a8\u00b5")
        buf.write("\u00c5\u00cc\u00d5\u00dc\u00e6\u00f1\u00fc\u0102\u0107")
        buf.write("\u010d\u0117\u0120\u0126\u012a\u0131\u013c\u0146\u014d")
        buf.write("\u0151\u015f\u016e\u0172\u017b\u0186\u018f\u0196\u019f")
        buf.write("\u01a3\u01ad\u01b3\u01ba\u01c5\u01d0\u01d6\u01db")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'null'", "'self'", "'contructor'", "'if'", 
                     "'else'", "'for'", "'continue'", "'break'", "'return'", 
                     "'void'", "'func'", "'new'", "'const'", "'var'", "'class'", 
                     "'{'", "'}'", "';'", "':'", "'<-'", "'='", "','", "'int'", 
                     "'float'", "'@'", "')'", "'('", "'['", "']'", "'^'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", 
                     "'||'", "'+'", "'-'", "'*'", "'/'", "'!'", "<INVALID>", 
                     "'%'", "'bool'", "'.'", "'string'", "':='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "NULL", "SELF", "CONTRUCTOR", "IF", "ELSE", 
                      "FOR", "CONTINUE", "BREAK", "RETURN", "VOID", "FUNCTION", 
                      "NEW", "CONST", "VAR", "CLASS", "LCB", "RCB", "SEMI", 
                      "COLON", "RARROW", "EQUAL", "COMMA", "INT", "FLOAT", 
                      "SIGN", "RB", "LB", "LSB", "RSB", "STRING_OP", "EQ_OP", 
                      "NEQ_OP", "LT_OP", "GT_OP", "LEQ_OP", "GEQ_OP", "AND_OP", 
                      "OR_OP", "ADD_OP", "SUB_OP", "MUL_OP", "F_DIV_OP", 
                      "NOT_OP", "I_DIV_OP", "REM_OP", "BOOL", "DOT", "STRING", 
                      "ASSGIN_OP", "INTLIT", "FLOATLIT", "BOOLLIT", "TRUE", 
                      "FALSE", "DIM", "STRINGLIT", "WS", "C_COMMENT", "CPP_COMMENT", 
                      "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_classbody = 2
    RULE_const_decl = 3
    RULE_full_form_const = 4
    RULE_var_decl = 5
    RULE_short_form = 6
    RULE_short_identifier_list = 7
    RULE_full_form = 8
    RULE_identifier_list = 9
    RULE_expression_list = 10
    RULE_expr = 11
    RULE_expr0 = 12
    RULE_expr1 = 13
    RULE_expr2 = 14
    RULE_expr3 = 15
    RULE_expr4 = 16
    RULE_expr5 = 17
    RULE_expr6 = 18
    RULE_expr7 = 19
    RULE_expr8 = 20
    RULE_expr9 = 21
    RULE_expr10 = 22
    RULE_expr11 = 23
    RULE_array_idx = 24
    RULE_index_expression = 25
    RULE_operands = 26
    RULE_subexpression = 27
    RULE_compare_ops = 28
    RULE_whole_type = 29
    RULE_core_type = 30
    RULE_id_type = 31
    RULE_at_id = 32
    RULE_arr_type = 33
    RULE_class_create = 34
    RULE_funct_declare = 35
    RULE_funct_prototype = 36
    RULE_params = 37
    RULE_parameter_list = 38
    RULE_parameter_declare = 39
    RULE_funct_body = 40
    RULE_function_call_stmt = 41
    RULE_function_call = 42
    RULE_function_call_params = 43
    RULE_function_call_param_list = 44
    RULE_funct_return_type = 45
    RULE_continue_statement = 46
    RULE_break_statement = 47
    RULE_return_statement = 48
    RULE_block_statement = 49
    RULE_stateVinhs = 50
    RULE_stateVinh = 51
    RULE_assignment_statement = 52
    RULE_assignment_content = 53
    RULE_lhs = 54
    RULE_assign_expressions = 55
    RULE_if_statement = 56
    RULE_pre_state = 57
    RULE_bool_expression = 58
    RULE_true_statements = 59
    RULE_else_expression = 60
    RULE_for_statement = 61
    RULE_for_body = 62

    ruleNames =  [ "program", "classdecl", "classbody", "const_decl", "full_form_const", 
                   "var_decl", "short_form", "short_identifier_list", "full_form", 
                   "identifier_list", "expression_list", "expr", "expr0", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "expr10", "expr11", "array_idx", 
                   "index_expression", "operands", "subexpression", "compare_ops", 
                   "whole_type", "core_type", "id_type", "at_id", "arr_type", 
                   "class_create", "funct_declare", "funct_prototype", "params", 
                   "parameter_list", "parameter_declare", "funct_body", 
                   "function_call_stmt", "function_call", "function_call_params", 
                   "function_call_param_list", "funct_return_type", "continue_statement", 
                   "break_statement", "return_statement", "block_statement", 
                   "stateVinhs", "stateVinh", "assignment_statement", "assignment_content", 
                   "lhs", "assign_expressions", "if_statement", "pre_state", 
                   "bool_expression", "true_statements", "else_expression", 
                   "for_statement", "for_body" ]

    EOF = Token.EOF
    NULL=1
    SELF=2
    CONTRUCTOR=3
    IF=4
    ELSE=5
    FOR=6
    CONTINUE=7
    BREAK=8
    RETURN=9
    VOID=10
    FUNCTION=11
    NEW=12
    CONST=13
    VAR=14
    CLASS=15
    LCB=16
    RCB=17
    SEMI=18
    COLON=19
    RARROW=20
    EQUAL=21
    COMMA=22
    INT=23
    FLOAT=24
    SIGN=25
    RB=26
    LB=27
    LSB=28
    RSB=29
    STRING_OP=30
    EQ_OP=31
    NEQ_OP=32
    LT_OP=33
    GT_OP=34
    LEQ_OP=35
    GEQ_OP=36
    AND_OP=37
    OR_OP=38
    ADD_OP=39
    SUB_OP=40
    MUL_OP=41
    F_DIV_OP=42
    NOT_OP=43
    I_DIV_OP=44
    REM_OP=45
    BOOL=46
    DOT=47
    STRING=48
    ASSGIN_OP=49
    INTLIT=50
    FLOATLIT=51
    BOOLLIT=52
    TRUE=53
    FALSE=54
    DIM=55
    STRINGLIT=56
    WS=57
    C_COMMENT=58
    CPP_COMMENT=59
    ID=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ClassdeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 126
                self.classdecl()
                self.state = 129 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 131
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def LCB(self):
            return self.getToken(CSlangParser.LCB, 0)

        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def id_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Id_typeContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Id_typeContext,i)


        def classbody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ClassbodyContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ClassbodyContext,i)


        def RARROW(self):
            return self.getToken(CSlangParser.RARROW, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = CSlangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(CSlangParser.CLASS)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 134
                self.id_type()
                pass

            elif la_ == 2:
                self.state = 135
                self.id_type()
                self.state = 136
                self.match(CSlangParser.RARROW)
                self.state = 137
                self.id_type()
                pass


            self.state = 141
            self.match(CSlangParser.LCB)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.FUNCTION) | (1 << CSlangParser.CONST) | (1 << CSlangParser.VAR))) != 0):
                self.state = 142
                self.classbody()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(CSlangParser.Var_declContext,0)


        def funct_declare(self):
            return self.getTypedRuleContext(CSlangParser.Funct_declareContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(CSlangParser.Const_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassbody" ):
                return visitor.visitClassbody(self)
            else:
                return visitor.visitChildren(self)




    def classbody(self):

        localctx = CSlangParser.ClassbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR]:
                self.state = 150
                self.var_decl()
                pass
            elif token in [CSlangParser.FUNCTION]:
                self.state = 151
                self.funct_declare()
                pass
            elif token in [CSlangParser.CONST]:
                self.state = 152
                self.const_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def full_form_const(self):
            return self.getTypedRuleContext(CSlangParser.Full_form_constContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = CSlangParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(CSlangParser.CONST)
            self.state = 156
            self.full_form_const()
            self.state = 157
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Full_form_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self):
            return self.getTypedRuleContext(CSlangParser.Id_typeContext,0)


        def identifier_list(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_full_form_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFull_form_const" ):
                return visitor.visitFull_form_const(self)
            else:
                return visitor.visitChildren(self)




    def full_form_const(self):

        localctx = CSlangParser.Full_form_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_full_form_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.id_type()
            self.state = 160
            self.identifier_list()
            self.state = 161
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def short_form(self):
            return self.getTypedRuleContext(CSlangParser.Short_formContext,0)


        def full_form(self):
            return self.getTypedRuleContext(CSlangParser.Full_formContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = CSlangParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(CSlangParser.VAR)
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 164
                self.short_form()
                pass

            elif la_ == 2:
                self.state = 165
                self.full_form()
                pass


            self.state = 168
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_formContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def short_identifier_list(self):
            return self.getTypedRuleContext(CSlangParser.Short_identifier_listContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def whole_type(self):
            return self.getTypedRuleContext(CSlangParser.Whole_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_short_form

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShort_form" ):
                return visitor.visitShort_form(self)
            else:
                return visitor.visitChildren(self)




    def short_form(self):

        localctx = CSlangParser.Short_formContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_short_form)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.short_identifier_list()
            self.state = 171
            self.match(CSlangParser.COLON)
            self.state = 172
            self.whole_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self):
            return self.getTypedRuleContext(CSlangParser.Id_typeContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def short_identifier_list(self):
            return self.getTypedRuleContext(CSlangParser.Short_identifier_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_short_identifier_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShort_identifier_list" ):
                return visitor.visitShort_identifier_list(self)
            else:
                return visitor.visitChildren(self)




    def short_identifier_list(self):

        localctx = CSlangParser.Short_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_short_identifier_list)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.id_type()
                self.state = 175
                self.match(CSlangParser.COMMA)
                self.state = 176
                self.short_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.id_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Full_formContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self):
            return self.getTypedRuleContext(CSlangParser.Id_typeContext,0)


        def identifier_list(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_full_form

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFull_form" ):
                return visitor.visitFull_form(self)
            else:
                return visitor.visitChildren(self)




    def full_form(self):

        localctx = CSlangParser.Full_formContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_full_form)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.id_type()
            self.state = 182
            self.identifier_list()
            self.state = 183
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def id_type(self):
            return self.getTypedRuleContext(CSlangParser.Id_typeContext,0)


        def identifier_list(self):
            return self.getTypedRuleContext(CSlangParser.Identifier_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def whole_type(self):
            return self.getTypedRuleContext(CSlangParser.Whole_typeContext,0)


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_identifier_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_list" ):
                return visitor.visitIdentifier_list(self)
            else:
                return visitor.visitChildren(self)




    def identifier_list(self):

        localctx = CSlangParser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_identifier_list)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(CSlangParser.COMMA)
                self.state = 186
                self.id_type()
                self.state = 187
                self.identifier_list()
                self.state = 188
                self.expr()
                self.state = 189
                self.match(CSlangParser.COMMA)
                pass
            elif token in [CSlangParser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(CSlangParser.COLON)
                self.state = 192
                self.whole_type()
                self.state = 193
                self.match(CSlangParser.EQUAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def expression_list(self):
            return self.getTypedRuleContext(CSlangParser.Expression_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = CSlangParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression_list)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.expr()
                self.state = 198
                self.match(CSlangParser.COMMA)
                self.state = 199
                self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self):
            return self.getTypedRuleContext(CSlangParser.Expr0Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CSlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.expr0()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr1Context,i)


        def STRING_OP(self):
            return self.getToken(CSlangParser.STRING_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr0" ):
                return visitor.visitExpr0(self)
            else:
                return visitor.visitChildren(self)




    def expr0(self):

        localctx = CSlangParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr0)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.expr1()
                self.state = 207
                self.match(CSlangParser.STRING_OP)
                self.state = 208
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr2Context,i)


        def compare_ops(self):
            return self.getTypedRuleContext(CSlangParser.Compare_opsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = CSlangParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr1)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.expr2(0)
                self.state = 214
                self.compare_ops()
                self.state = 215
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def AND_OP(self):
            return self.getToken(CSlangParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(CSlangParser.OR_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.AND_OP or _la==CSlangParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.expr3(0) 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def ADD_OP(self):
            return self.getToken(CSlangParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(CSlangParser.SUB_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 234
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 235
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD_OP or _la==CSlangParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 236
                    self.expr4(0) 
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def MUL_OP(self):
            return self.getToken(CSlangParser.MUL_OP, 0)

        def F_DIV_OP(self):
            return self.getToken(CSlangParser.F_DIV_OP, 0)

        def REM_OP(self):
            return self.getToken(CSlangParser.REM_OP, 0)

        def I_DIV_OP(self):
            return self.getToken(CSlangParser.I_DIV_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 245
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 246
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MUL_OP) | (1 << CSlangParser.F_DIV_OP) | (1 << CSlangParser.I_DIV_OP) | (1 << CSlangParser.REM_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 247
                    self.expr5() 
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(CSlangParser.NOT_OP, 0)

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = CSlangParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr5)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(CSlangParser.NOT_OP)
                self.state = 254
                self.expr5()
                pass
            elif token in [CSlangParser.NEW, CSlangParser.SIGN, CSlangParser.LB, CSlangParser.SUB_OP, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRINGLIT, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(CSlangParser.SUB_OP, 0)

        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr6)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(CSlangParser.SUB_OP)
                self.state = 259
                self.expr6()
                pass
            elif token in [CSlangParser.NEW, CSlangParser.SIGN, CSlangParser.LB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRINGLIT, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def index_expression(self):
            return self.getTypedRuleContext(CSlangParser.Index_expressionContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = CSlangParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr7)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.expr8(0)
                self.state = 264
                self.index_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    self.match(CSlangParser.DOT)
                    self.state = 274
                    self.expr9() 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr10Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr10Context,i)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def SIGN(self):
            return self.getToken(CSlangParser.SIGN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = CSlangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr9)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.expr10()
                self.state = 281
                self.match(CSlangParser.DOT)
                self.state = 282
                self.match(CSlangParser.SIGN)
                self.state = 283
                self.expr10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_create(self):
            return self.getTypedRuleContext(CSlangParser.Class_createContext,0)


        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def expr11(self):
            return self.getTypedRuleContext(CSlangParser.Expr11Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr10)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.class_create()
                self.state = 289
                self.expr10()
                pass
            elif token in [CSlangParser.SIGN, CSlangParser.LB, CSlangParser.INTLIT, CSlangParser.FLOATLIT, CSlangParser.BOOLLIT, CSlangParser.STRINGLIT, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_idx(self):
            return self.getTypedRuleContext(CSlangParser.Array_idxContext,0)


        def operands(self):
            return self.getTypedRuleContext(CSlangParser.OperandsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = CSlangParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr11)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.array_idx()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_idxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self):
            return self.getTypedRuleContext(CSlangParser.Id_typeContext,0)


        def index_expression(self):
            return self.getTypedRuleContext(CSlangParser.Index_expressionContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_idx

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_idx" ):
                return visitor.visitArray_idx(self)
            else:
                return visitor.visitChildren(self)




    def array_idx(self):

        localctx = CSlangParser.Array_idxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_idx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.id_type()
            self.state = 299
            self.index_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(CSlangParser.LSB, 0)

        def RSB(self):
            return self.getToken(CSlangParser.RSB, 0)

        def expression_list(self):
            return self.getTypedRuleContext(CSlangParser.Expression_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)




    def index_expression(self):

        localctx = CSlangParser.Index_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_index_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(CSlangParser.LSB)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NEW) | (1 << CSlangParser.SIGN) | (1 << CSlangParser.LB) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID))) != 0):
                self.state = 302
                self.expression_list()


            self.state = 305
            self.match(CSlangParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(CSlangParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(CSlangParser.STRINGLIT, 0)

        def function_call(self):
            return self.getTypedRuleContext(CSlangParser.Function_callContext,0)


        def id_type(self):
            return self.getTypedRuleContext(CSlangParser.Id_typeContext,0)


        def subexpression(self):
            return self.getTypedRuleContext(CSlangParser.SubexpressionContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = CSlangParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_operands)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(CSlangParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(CSlangParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 309
                self.match(CSlangParser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 310
                self.match(CSlangParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 311
                self.function_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 312
                self.id_type()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 313
                self.subexpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_subexpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpression" ):
                return visitor.visitSubexpression(self)
            else:
                return visitor.visitChildren(self)




    def subexpression(self):

        localctx = CSlangParser.SubexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_subexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(CSlangParser.LB)
            self.state = 317
            self.expr()
            self.state = 318
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compare_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_OP(self):
            return self.getToken(CSlangParser.EQ_OP, 0)

        def NEQ_OP(self):
            return self.getToken(CSlangParser.NEQ_OP, 0)

        def LT_OP(self):
            return self.getToken(CSlangParser.LT_OP, 0)

        def GT_OP(self):
            return self.getToken(CSlangParser.GT_OP, 0)

        def LEQ_OP(self):
            return self.getToken(CSlangParser.LEQ_OP, 0)

        def GEQ_OP(self):
            return self.getToken(CSlangParser.GEQ_OP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_compare_ops

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare_ops" ):
                return visitor.visitCompare_ops(self)
            else:
                return visitor.visitChildren(self)




    def compare_ops(self):

        localctx = CSlangParser.Compare_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_compare_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQ_OP) | (1 << CSlangParser.NEQ_OP) | (1 << CSlangParser.LT_OP) | (1 << CSlangParser.GT_OP) | (1 << CSlangParser.LEQ_OP) | (1 << CSlangParser.GEQ_OP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Whole_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def core_type(self):
            return self.getTypedRuleContext(CSlangParser.Core_typeContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(CSlangParser.Arr_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_whole_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhole_type" ):
                return visitor.visitWhole_type(self)
            else:
                return visitor.visitChildren(self)




    def whole_type(self):

        localctx = CSlangParser.Whole_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_whole_type)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.core_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.arr_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Core_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def arr_type(self):
            return self.getTypedRuleContext(CSlangParser.Arr_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_core_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCore_type" ):
                return visitor.visitCore_type(self)
            else:
                return visitor.visitChildren(self)




    def core_type(self):

        localctx = CSlangParser.Core_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_core_type)
        try:
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 329
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.LCB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 330
                self.arr_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def at_id(self):
            return self.getTypedRuleContext(CSlangParser.At_idContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_id_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_type" ):
                return visitor.visitId_type(self)
            else:
                return visitor.visitChildren(self)




    def id_type(self):

        localctx = CSlangParser.Id_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_id_type)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.SIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.at_id()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class At_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGN(self):
            return self.getToken(CSlangParser.SIGN, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_at_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAt_id" ):
                return visitor.visitAt_id(self)
            else:
                return visitor.visitChildren(self)




    def at_id(self):

        localctx = CSlangParser.At_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_at_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(CSlangParser.SIGN)
            self.state = 338
            self.match(CSlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(CSlangParser.LCB, 0)

        def DIM(self):
            return self.getToken(CSlangParser.DIM, 0)

        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def core_type(self):
            return self.getTypedRuleContext(CSlangParser.Core_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = CSlangParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(CSlangParser.LCB)
            self.state = 341
            self.match(CSlangParser.DIM)
            self.state = 342
            self.match(CSlangParser.RCB)
            self.state = 343
            self.core_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def whole_type(self):
            return self.getTypedRuleContext(CSlangParser.Whole_typeContext,0)


        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def expression_list(self):
            return self.getTypedRuleContext(CSlangParser.Expression_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_create

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_create" ):
                return visitor.visitClass_create(self)
            else:
                return visitor.visitChildren(self)




    def class_create(self):

        localctx = CSlangParser.Class_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_class_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(CSlangParser.NEW)
            self.state = 346
            self.whole_type()
            self.state = 347
            self.match(CSlangParser.LB)
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NEW) | (1 << CSlangParser.SIGN) | (1 << CSlangParser.LB) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID))) != 0):
                self.state = 348
                self.expression_list()


            self.state = 351
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(CSlangParser.FUNCTION, 0)

        def funct_prototype(self):
            return self.getTypedRuleContext(CSlangParser.Funct_prototypeContext,0)


        def funct_body(self):
            return self.getTypedRuleContext(CSlangParser.Funct_bodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_funct_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunct_declare" ):
                return visitor.visitFunct_declare(self)
            else:
                return visitor.visitChildren(self)




    def funct_declare(self):

        localctx = CSlangParser.Funct_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_funct_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(CSlangParser.FUNCTION)
            self.state = 354
            self.funct_prototype()

            self.state = 355
            self.funct_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_prototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self):
            return self.getTypedRuleContext(CSlangParser.Id_typeContext,0)


        def params(self):
            return self.getTypedRuleContext(CSlangParser.ParamsContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def funct_return_type(self):
            return self.getTypedRuleContext(CSlangParser.Funct_return_typeContext,0)


        def CONTRUCTOR(self):
            return self.getToken(CSlangParser.CONTRUCTOR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_funct_prototype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunct_prototype" ):
                return visitor.visitFunct_prototype(self)
            else:
                return visitor.visitChildren(self)




    def funct_prototype(self):

        localctx = CSlangParser.Funct_prototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_funct_prototype)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SIGN, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.id_type()
                self.state = 358
                self.params()
                self.state = 359
                self.match(CSlangParser.COLON)
                self.state = 360
                self.funct_return_type()
                pass
            elif token in [CSlangParser.CONTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(CSlangParser.CONTRUCTOR)
                self.state = 363
                self.params()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(CSlangParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = CSlangParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(CSlangParser.LB)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.SIGN or _la==CSlangParser.ID:
                self.state = 367
                self.parameter_list()


            self.state = 370
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_declare(self):
            return self.getTypedRuleContext(CSlangParser.Parameter_declareContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(CSlangParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = CSlangParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_parameter_list)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.parameter_declare()
                self.state = 373
                self.match(CSlangParser.COMMA)
                self.state = 374
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.parameter_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self):
            return self.getTypedRuleContext(CSlangParser.Id_typeContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def whole_type(self):
            return self.getTypedRuleContext(CSlangParser.Whole_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_parameter_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declare" ):
                return visitor.visitParameter_declare(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declare(self):

        localctx = CSlangParser.Parameter_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_parameter_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.id_type()
            self.state = 380
            self.match(CSlangParser.COLON)
            self.state = 381
            self.whole_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_funct_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunct_body" ):
                return visitor.visitFunct_body(self)
            else:
                return visitor.visitChildren(self)




    def funct_body(self):

        localctx = CSlangParser.Funct_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_funct_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Id_typeContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Id_typeContext,i)


        def function_call_params(self):
            return self.getTypedRuleContext(CSlangParser.Function_call_paramsContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_function_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_stmt" ):
                return visitor.visitFunction_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def function_call_stmt(self):

        localctx = CSlangParser.Function_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_function_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 385
                self.id_type()
                self.state = 386
                self.match(CSlangParser.DOT)


            self.state = 390
            self.id_type()
            self.state = 391
            self.function_call_params()
            self.state = 392
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Id_typeContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Id_typeContext,i)


        def function_call_params(self):
            return self.getTypedRuleContext(CSlangParser.Function_call_paramsContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = CSlangParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 394
                self.id_type()
                self.state = 395
                self.match(CSlangParser.DOT)


            self.state = 399
            self.id_type()
            self.state = 400
            self.function_call_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def function_call_param_list(self):
            return self.getTypedRuleContext(CSlangParser.Function_call_param_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_function_call_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_params" ):
                return visitor.visitFunction_call_params(self)
            else:
                return visitor.visitChildren(self)




    def function_call_params(self):

        localctx = CSlangParser.Function_call_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_function_call_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(CSlangParser.LB)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NEW) | (1 << CSlangParser.SIGN) | (1 << CSlangParser.LB) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID))) != 0):
                self.state = 403
                self.function_call_param_list()


            self.state = 406
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(CSlangParser.COMMA, 0)

        def function_call_param_list(self):
            return self.getTypedRuleContext(CSlangParser.Function_call_param_listContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_function_call_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_param_list" ):
                return visitor.visitFunction_call_param_list(self)
            else:
                return visitor.visitChildren(self)




    def function_call_param_list(self):

        localctx = CSlangParser.Function_call_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_function_call_param_list)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.expr()
                self.state = 409
                self.match(CSlangParser.COMMA)
                self.state = 410
                self.function_call_param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funct_return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def core_type(self):
            return self.getTypedRuleContext(CSlangParser.Core_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_funct_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunct_return_type" ):
                return visitor.visitFunct_return_type(self)
            else:
                return visitor.visitChildren(self)




    def funct_return_type(self):

        localctx = CSlangParser.Funct_return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_funct_return_type)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.match(CSlangParser.VOID)
                pass
            elif token in [CSlangParser.LCB, CSlangParser.INT, CSlangParser.FLOAT, CSlangParser.BOOL, CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.core_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = CSlangParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(CSlangParser.CONTINUE)
            self.state = 420
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = CSlangParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(CSlangParser.BREAK)
            self.state = 423
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = CSlangParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(CSlangParser.RETURN)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NEW) | (1 << CSlangParser.SIGN) | (1 << CSlangParser.LB) | (1 << CSlangParser.SUB_OP) | (1 << CSlangParser.NOT_OP) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRINGLIT) | (1 << CSlangParser.ID))) != 0):
                self.state = 426
                self.expr()


            self.state = 429
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(CSlangParser.LCB, 0)

        def RCB(self):
            return self.getToken(CSlangParser.RCB, 0)

        def stateVinhs(self):
            return self.getTypedRuleContext(CSlangParser.StateVinhsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = CSlangParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(CSlangParser.LCB)
            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.LCB) | (1 << CSlangParser.SIGN) | (1 << CSlangParser.ID))) != 0):
                self.state = 432
                self.stateVinhs()


            self.state = 435
            self.match(CSlangParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateVinhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stateVinh(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StateVinhContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StateVinhContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_stateVinhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateVinhs" ):
                return visitor.visitStateVinhs(self)
            else:
                return visitor.visitChildren(self)




    def stateVinhs(self):

        localctx = CSlangParser.StateVinhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_stateVinhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 437
                self.stateVinh()
                self.state = 440 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.VAR) | (1 << CSlangParser.LCB) | (1 << CSlangParser.SIGN) | (1 << CSlangParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateVinhContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_statement(self):
            return self.getTypedRuleContext(CSlangParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(CSlangParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(CSlangParser.For_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(CSlangParser.Return_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(CSlangParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(CSlangParser.Continue_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(CSlangParser.Var_declContext,0)


        def function_call_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Function_call_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_stateVinh

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateVinh" ):
                return visitor.visitStateVinh(self)
            else:
                return visitor.visitChildren(self)




    def stateVinh(self):

        localctx = CSlangParser.StateVinhContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_stateVinh)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.assignment_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 444
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 445
                self.return_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 446
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 447
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 448
                self.block_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 449
                self.var_decl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 450
                self.function_call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_content(self):
            return self.getTypedRuleContext(CSlangParser.Assignment_contentContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = CSlangParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.assignment_content()
            self.state = 454
            self.match(CSlangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def ASSGIN_OP(self):
            return self.getToken(CSlangParser.ASSGIN_OP, 0)

        def assign_expressions(self):
            return self.getTypedRuleContext(CSlangParser.Assign_expressionsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assignment_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_content" ):
                return visitor.visitAssignment_content(self)
            else:
                return visitor.visitChildren(self)




    def assignment_content(self):

        localctx = CSlangParser.Assignment_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_assignment_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.lhs()
            self.state = 457
            self.match(CSlangParser.ASSGIN_OP)
            self.state = 458
            self.assign_expressions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_type(self):
            return self.getTypedRuleContext(CSlangParser.Id_typeContext,0)


        def array_idx(self):
            return self.getTypedRuleContext(CSlangParser.Array_idxContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = CSlangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_lhs)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.id_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.array_idx()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_expressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assign_expressions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_expressions" ):
                return visitor.visitAssign_expressions(self)
            else:
                return visitor.visitChildren(self)




    def assign_expressions(self):

        localctx = CSlangParser.Assign_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_assign_expressions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def bool_expression(self):
            return self.getTypedRuleContext(CSlangParser.Bool_expressionContext,0)


        def true_statements(self):
            return self.getTypedRuleContext(CSlangParser.True_statementsContext,0)


        def pre_state(self):
            return self.getTypedRuleContext(CSlangParser.Pre_stateContext,0)


        def else_expression(self):
            return self.getTypedRuleContext(CSlangParser.Else_expressionContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = CSlangParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(CSlangParser.IF)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LCB:
                self.state = 467
                self.pre_state()


            self.state = 470
            self.bool_expression()
            self.state = 471
            self.true_statements()
            self.state = 473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 472
                self.else_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pre_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_pre_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPre_state" ):
                return visitor.visitPre_state(self)
            else:
                return visitor.visitChildren(self)




    def pre_state(self):

        localctx = CSlangParser.Pre_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_pre_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_bool_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expression" ):
                return visitor.visitBool_expression(self)
            else:
                return visitor.visitChildren(self)




    def bool_expression(self):

        localctx = CSlangParser.Bool_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_bool_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class True_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_true_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue_statements" ):
                return visitor.visitTrue_statements(self)
            else:
                return visitor.visitChildren(self)




    def true_statements(self):

        localctx = CSlangParser.True_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_true_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_else_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_expression" ):
                return visitor.visitElse_expression(self)
            else:
                return visitor.visitChildren(self)




    def else_expression(self):

        localctx = CSlangParser.Else_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_else_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(CSlangParser.ELSE)
            self.state = 482
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assignment_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Assignment_statementContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Assignment_statementContext,i)


        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(CSlangParser.SEMI, 0)

        def for_body(self):
            return self.getTypedRuleContext(CSlangParser.For_bodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = CSlangParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(CSlangParser.FOR)
            self.state = 485
            self.assignment_statement()
            self.state = 486
            self.expr()
            self.state = 487
            self.match(CSlangParser.SEMI)
            self.state = 488
            self.assignment_statement()
            self.state = 489
            self.for_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_statement(self):
            return self.getTypedRuleContext(CSlangParser.Block_statementContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_body" ):
                return visitor.visitFor_body(self)
            else:
                return visitor.visitChildren(self)




    def for_body(self):

        localctx = CSlangParser.For_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_for_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expr2_sempred
        self._predicates[15] = self.expr3_sempred
        self._predicates[16] = self.expr4_sempred
        self._predicates[20] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




