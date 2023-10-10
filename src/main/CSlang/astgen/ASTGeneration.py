from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *


class ASTGeneration(CSlangVisitor):

    def visitProgram(self, ctx: CSlangParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])

    def visitClassdecl(self, ctx: CSlangParser.ClassdeclContext):
        if (ctx.classbody()):
            if (ctx.RARROW):
                return ClassDecl((self.visit(ctx.id_type(0))), [self.visit(x) for x in ctx.classbody()], (self.visit(ctx.id_type(0))))
            else:
                return ClassDecl((self.visit(ctx.id_type())), [self.visit(x) for x in ctx.classbody()])
        else:

            return ClassDecl((self.visit(ctx.id_type(0))), [])

    def visitClassbody(self, ctx: CSlangParser.ClassbodyContext):
        return self.visit(ctx.getChild(0))

    def visitVar_decl(self, ctx: CSlangParser.Var_declContext):
        if (ctx.short_form()):
            return self.visit(ctx.short_form())
        else:
            return self.visit(ctx.full_form())

    def visitShort_form(self, ctx: CSlangParser.Short_formContext):
        return VarDecl(self.visit(ctx.short_identifier_list()), self.visit(ctx.whole_type()))

    def visitShort_identifier_list(self, ctx: CSlangParser.Short_identifier_listContext):
        return [self.visit(x) for x in ctx.id_type()]

    def visitFull_form(self, ctx: CSlangParser.Full_formContext):
        id_list = [self.visit(x) for x in ctx.id_type()]
        temp_list = self.visit(ctx.identifier_list())
        var_type = temp_list[-1]
        temp_list = temp_list[:-1]
        id_list = id_list + [tuple[0] for tuple in temp_list]
        expr_list = [self.visit(ctx.expr())] + [tuple[1]
                                                for tuple in temp_list]
        res = [VarDecl(id_list[i], var_type, expr_list[len(id_list)-i-1])
               for i in range(len(id_list))]
        return res

    def visitIdentifier_list(self, ctx: CSlangParser.Identifier_listContext):
        if (ctx.id_type()):
            return [(ctx.id_type(), self.visit(ctx.expr()))] + self.visit(ctx.identifier_list())
        return [self.visit(ctx.whole_type())]

    def visitExpression_list(self, ctx: CSlangParser.Expression_listContext):
        return [self.visit(x) for x in ctx.expr()]

    def visitExpr(self, ctx: CSlangParser.ExprContext):
        return self.visit(ctx.expr0())

    def visitExpr0(self, ctx: CSlangParser.Expr0Context):
        if (ctx.getChildCount() == 3):
            return BinaryOP(ctx.STRING_OP().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        else:
            return self.visit(ctx.expr1())

    def visitExpr1(self, ctx: CSlangParser.Expr1Context):
        if (ctx.getChildCount() == 3):
            return BinaryOP(self.visit(ctx.compare_ops()), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        else:
            return self.visit(ctx.expr2())

    def visitExpr2(self, ctx: CSlangParser.Expr2Context):
        if (ctx.getChildCount() == 3):
            return BinaryOP(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())

    def visitExpr3(self, ctx: CSlangParser.Expr3Context):
        if (ctx.getChildCount() == 3):
            return BinaryOP(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())

    def visitExpr4(self, ctx: CSlangParser.Expr4Context):
        if (ctx.getChildCount() == 3):
            return BinaryOP(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())

    def visitExpr5(self, ctx: CSlangParser.Expr5Context):
        if (ctx.getChildCount() == 2):
            return UnaryOP(ctx.NOT_OP().getText(), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr6())

    def visitExpr6(self, ctx: CSlangParser.Expr6Context):
        if (ctx.getChildCount() == 2):
            return UnaryOP(ctx.SUB_OP().getText(), self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr7())

    def visitExpr7(self, ctx: CSlangParser.Expr7Context):
        if (ctx.index_expression()):
            return UnaryOP(self.visit(ctx.index_expression()), self.visit(ctx.expr8()))
        else:
            return self.visit(ctx.expr8())

    def visitExpr8(self, ctx: CSlangParser.Expr8Context):
        if (ctx.DOT()):
            return FieldAccess(self.visit(ctx.expr8()), self.visit(ctx.expr9()))
        else:
            return self.visit(ctx.expr9())

    def visitExpr9(self, ctx: CSlangParser.Expr9Context):
        if (ctx.DOT()):
            return FieldAccess(self.visit(ctx.expr10(0)), self.visit(ctx.expr10(1)))
        else:
            return self.visit(ctx.expr10())

    def visitExpr10(self, ctx: CSlangParser.Expr10Context):
        if (ctx.getChildCount == 2):
            return NewExpr(self.visit(ctx.expr10()), self.visit(ctx.class_create()))
        else:
            return self.visit(ctx.expr11())

    def visitExpr11(self, ctx: CSlangParser.Expr11Context):
        return self.visit(ctx.getChild(0))

    def visitOperands(self, ctx: CSlangParser.OperandsContext):
        if (ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif (ctx.FLOATLIT()):
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif (ctx.BOOLLIT()):
            return BooleanLiteral(bool(ctx.BOOLLIT().getText()))
        elif (ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT.getText())
        else:
            return self.visit(ctx.getChild(0))

    def visitArray_idx(self, ctx: CSlangParser.Array_idxContext):
        return ArrayCell(self.visit(ctx.id_type()), self.visit(ctx.index_expression()))

    def visitIndex_expression(self, ctx: CSlangParser.Index_expressionContext):
        if (ctx.expression_list()):
            return self.visit(ctx.expression_list())
        else:
            return Expr()

    def visitCompare_ops(self, ctx: CSlangParser.Compare_opsContext):
        return ctx.getChild(0).getText()

    def visitWhole_type(self, ctx: CSlangParser.Whole_typeContext):
        if (ctx.core_type()):
            return self.visit(ctx.core_type())
        else:
            return self.visit(ctx.arr_type())

    def visitCore_type(self, ctx: CSlangParser.Core_typeContext):
        if (ctx.arr_type()):
            return self.visit(ctx.arr_type())
        elif (ctx.INT()):
            return IntType()
        elif (ctx.FLOAT()):
            return FloatType()
        elif (ctx.BOOL()):
            return BoolType()
        elif (ctx.STRING()):
            return StringType()

    def visitArr_type(self, ctx: CSlangParser.Arr_typeContext):
        return ArrayType(int(ctx.DIM().getText()), self.visit(ctx.core_type()))
    def visitId_type(self,ctx:CSlangParser.Id_typeContext):
        if(ctx.ID()):
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.at_id())
    def visitAt_id(self,ctx:CSlangParser.At_idContext):
        return Id(ctx.SIGN().getText()+ctx.ID().getText())
    def visitFunction_call(self,ctx:CSlangParser.Function_callContext):
        return CallStmt(self.visit(ctx.id_type()),self.visit(ctx.function_call_params()))
    def visitConst_decl(self,ctx:CSlangParser.Const_declContext):
        return self.visit(ctx.full_form_const())
    def visitFull_form_const(self,ctx:CSlangParser.Full_form_constContext):
        id_list = [self.visit(x) for x in ctx.id_type()]
        temp_list = self.visit(ctx.identifier_list())
        var_type = temp_list[-1]
        temp_list = temp_list[:-1]
        id_list = id_list + [tuple[0] for tuple in temp_list]
        expr_list = [self.visit(ctx.expr())] + [tuple[1]
                                                for tuple in temp_list]
        res = [ConstDecl(id_list[i], var_type, expr_list[len(id_list)-i-1])
               for i in range(len(id_list))]
        return res
    def visitFunction_call_params(self,ctx:CSlangParser.Function_call_paramsContext):
        if(ctx.function_call_param_list()):
            return self.visit(ctx.function_call_param_list())
        else:
            return []
    def visitFunction_call_param_list(self,ctx:CSlangParser.Function_call_param_listContext):
        return Expr([self.visit(x) for x in ctx.expr()])
    def visitFunc_declare(self,ctx:CSlangParser.Funct_declareContext):
        protype = self.visit(ctx.funct_prototype())
        function_body = self.visit(ctx.funct_body())
        return MethodDecl(protype[0], protype[1], protype[2],  function_body)
    def visitFunct_prototype(self,ctx:CSlangParser.Funct_prototypeContext):
        if(ctx.CONTRUCTOR()):
            return (Id(ctx.CONTRUCTOR().getText()),self.visit(ctx.params()))
        else:
            return (self.visit(ctx.id_type()),self.visit(ctx.params()),self.visit(ctx.funct_return_type()))
    def visitFunct_return_type(self,ctx:CSlangParser.Funct_return_typeCOntext):
        if(ctx.VOID()):
            return VoidType()
        else:
            return self.visit(ctx.core_type())
    def visitParams(self,ctx:CSlangParser.ParamsContext):
        if(ctx.parameter_list()):
            return self.visit(ctx.parameter_list())
        else:
            return []
    def visitParameter_list(self,ctx:CSlangParser.Parameter_listContext):
        if (ctx.getChildCount() == 3):
            return [self.visit(ctx.parameter_declare())] + self.visit(ctx.parameter_list())
        return [self.visit(ctx.parameter_declare())]
    def visitParameter_declare(self,ctx:CSlangParser.Parameter_declareContext):
        res = []
        res.append(ctx.IDENTIFIER())
        res.append(self.visit(ctx.var_type()))
        return res
    def visitFunct_body(self,ctx:CSlangParser.Funct_bodyContext):
        return self.visit(ctx.block_statement())
    def visitContinue_statement(self,ctx:CSlangParser.Continue_statementContext):
        return Continue()
    def visitBreak_statement(self,ctx:CSlangParser.Break_statementContext):
        return Break()
    def visitBlock_statement(self,ctx:CSlangParser.Block_statementContext):
        if(ctx.stateVinhs()):
            return self.visit(ctx.stateVinhs())
        else:
            return None
    def visitStateVinhs(self,ctx:CSlangParser.StateVinhsContext):
        return Block([self.visit(x) for x in ctx.stateVinh()])
    def visitStateVinh(self,ctx:CSlangParser.StateVinhContext):
        return self.visit(ctx.getChild(0))
    def visitReturn_statement(self,ctx:CSlangParser.Return_statementContext):
        if(ctx.expr()):
            return Return(self.visit(ctx.expr()))
        else: 
            return Return()
    def visitAssignment_statement(self, ctx: CSlangParser.Assignment_statementContext):
        assignment_content = self.visit(ctx.assignment_content())
        return Assign(assignment_content[0], assignment_content[1])

    def visitAssignment_content(self, ctx: CSlangParser.Assignment_contentContext):
        return (self.visit(ctx.lhs()), self.visit(ctx.assign_expressions()))

    def visitLhs(self, ctx: CSlangParser.LhsContext):
        if (ctx.id_type()):
            return self.visit(ctx.id_type())
        return self.visit(ctx.array_idx())

    def visitAssign_expressions(self, ctx: CSlangParser.Assign_expressionsContext):
        return self.visit(ctx.expr())
    def visitIf_statement(self, ctx: CSlangParser.If_statementContext):
        bool_expression = self.visit(ctx.bool_expression())
        true_statements = self.visit(ctx.true_statements())
        if(ctx.pre_state()):
             pre_state=self.visit(ctx.pre_state)
        
        else_expression = self.visit(
            ctx.else_expression()) if ctx.else_expression() else None
        if(ctx.pre_state()):
            return If(bool_expression, true_statements, pre_state,else_expression)
        else:
             return If(bool_expression, true_statements,else_expression)
    def visitBool_expression(self, ctx: CSlangParser.Bool_expressionContext):
        return self.visit(ctx.expr())

    def visitTrue_statements(self, ctx: CSlangParser.True_statementsContext):
        return self.visit(ctx.block_statement())

    def visitElse_expression(self, ctx: CSlangParser.Else_expressionContext):
        return self.visit(ctx.block_statement())
    def visitPre_state(self,ctx:CSlangParser.Pre_stateContext):
        return self.visit(ctx.block_statement())
    def visitFor_statement(self, ctx: CSlangParser.For_statementContext):
        cond = self.visit(ctx.expr())
        upd = self.visit(ctx.assignment_statement(1))
        for_body = self.visit(ctx.for_body())
        return For(self.visit(ctx.assignment_statement(0)), cond, upd, for_body)

    def visitFor_body(self, ctx: CSlangParser.For_bodyContext):
        return (self.visit(ctx.block_statement()))
    
    
        
        