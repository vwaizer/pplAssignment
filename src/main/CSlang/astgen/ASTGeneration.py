from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):

    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])

    def visitClassdecl(self,ctx:CSlangParser.ClassdeclContext):
        if(ctx.classbody()):
            if(ctx.RARROW):
                return ClassDecl((self.visit(ctx.id_type(0))),[self.visit(x) for x in ctx.classbody()],(self.visit(ctx.id_type(0))))
            else:
                return ClassDecl((self.visit(ctx.id_type())),[self.visit(x) for x in ctx.classbody()])
        else:

            return ClassDecl((self.visit(ctx.id_type(0))),[])

    def visitClassbody(self,ctx:CSlangParser.ClassbodyContext):
        return self.visit(ctx.getChild(0))
    
    def visitVar_decl(self,ctx:CSlangParser.Var_declContext):
        if(ctx.short_form()):
            return self.visit(ctx.short_form())
        else:
            return self.visit(ctx.full_form())
    def visitShort_form(self,ctx:CSlangParser.Short_formContext):
        return VarDecl(self.visit(ctx.short_identifier_list()),self.visit(ctx.whole_type()))
    def visitShort_identifier_list(self,ctx:CSlangParser.Short_identifier_listContext):
        return [self.visit(x) for x in ctx.id_type() ]
    def visitFull_form(self,ctx:CSlangParser.Full_formContext):
        id_list = [self.visit(x) for x in ctx.id_type()]
        temp_list = self.visit(ctx.identifier_list())
        var_type = temp_list[-1]
        temp_list = temp_list[:-1]
        id_list = id_list + [tuple[0] for tuple in temp_list]
        expr_list = [self.visit(ctx.expr())] + [tuple[1] for tuple in temp_list]
        res = [VarDecl(id_list[i], var_type, expr_list[len(id_list)-i-1]) for i in range(len(id_list))]
        # for val in res:
        #   print(val)
        return res
    def visitIdentifier_list(self, ctx: CSlangParser.Identifier_listContext):
        if (ctx.id_type()):
            return [(ctx.id_type(), self.visit(ctx.expr()))] + self.visit(ctx.identifier_list())
        return [self.visit(ctx.whole_type())]
    def visitExpression_list(self,ctx:CSlangParser.Expression_listContext):
        return [self.visit(x) for x in ctx.expr()]
    def visitExpr(self,ctx:CSlangParser.ExprContext):
        return self.visit(ctx.expr0())
    def visitExpr0(self,ctx:CSlangParser.Expr0Context):
        if(ctx.getChildCount() == 3):
            return BinaryOP(ctx.STRING_OP().getText(),self.visit(ctx.expr1(0)),self.visit(ctx.expr1(1)))
        else:
            return self.visit(ctx.expr1())
    def visitExpr1(self,ctx:CSlangParser.Expr1Context):
        if(ctx.getChildCount()==3):
            return BinaryOP(self.visit(ctx.compare_ops()),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))
        else:
            return self.visit(ctx.expr2())
    def visitExpr2(self,ctx:CSlangParser.Expr2Context):
        if(ctx.getChildCount()==3):
            return BinaryOP(ctx.getChild(1).getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())
    def visitExpr3(self,ctx:CSlangParser.Expr3Context):
        if(ctx.getChildCount()==3):
            return BinaryOP(ctx.getChild(1).getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())
    def visitExpr4(self,ctx:CSlangParser.Expr4Context):
        if(ctx.getChildCount()==3):
            return BinaryOP(ctx.getChild(1).getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())
    def visitExpr5(self,ctx:CSlangParser.Expr5Context):
        if(ctx.getChildCount()==2):
            return UnaryOP(ctx.NOT_OP().getText(),self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr6())
    def visitExpr6(self,ctx:CSlangParser.Expr6Context):
        if(ctx.getChildCount()==2):
            return UnaryOP(ctx.SUB_OP().getText(),self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr7())
    def visitExpr7(self,ctx:CSlangParser.Expr7Context):
        if(ctx.index_expression()):
            return UnaryOP(self.visit(ctx.index_expression()),self.visit(ctx.expr8()))
        else:
            return self.visit(ctx.expr8())
    def visitExpr8(self,ctx:CSlangParser.Expr8Context):
        if(ctx.DOT()):
            return FieldAccess(self.visit(ctx.expr8()),self.visit(ctx.expr9()))
        else:
            return self.visit(ctx.expr9())
    def visitExpr9(self,ctx:CSlangParser.Expr9Context):
        if(ctx.DOT()):
            return FieldAccess(self.visit(ctx.expr10(0)),self.visit(ctx.expr10(1)))
        else:
            return self.visit(ctx.expr10())
    def visitExpr10(self,ctx:CSlangParser.Expr10Context):
        if(ctx.getChildCount==2):
            return NewExpr(self.visit(ctx.expr10()),self.visit(ctx.class_create()))
        else:
            return self.visit(ctx.expr11())
    def visitExpr11(self,ctx:CSlangParser.Expr11Context):
        return self.visit(ctx.getChild(0))
    def visitOperands(self,ctx:CSlangParser.OperandsContext):
        if(ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif (ctx.FLOATLIT()):
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif(ctx.BOOLLIT()):
            return BooleanLiteral(bool(ctx.BOOLLIT().getText()))
        elif(ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT.getText())
        else:
            return self.visit(ctx.getChild(0))
    def visitArray_idx(self,ctx:CSlangParser.Array_idxContext):
        return ArrayCell(self.visit(ctx.id_type()),self.visit(ctx.index_expression()))
    def visitIndex_expression(self,ctx:CSlangParser.Index_expressionContext):
        if(ctx.expression_list()):
            return self.visit(ctx.expression_list())
        else: return Expr()
    def visitCompare_ops(self,ctx:CSlangParser.Compare_opsContext):
        return ctx.getChild(0).getText()
    
    
        

    
        
    
    
        

    
