# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classdecl.
    def visitClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#memdecl.
    def visitMemdecl(self, ctx:CSlangParser.MemdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#cslangtype.
    def visitCslangtype(self, ctx:CSlangParser.CslangtypeContext):
        return self.visitChildren(ctx)



del CSlangParser