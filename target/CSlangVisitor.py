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


    # Visit a parse tree produced by CSlangParser#classbody.
    def visitClassbody(self, ctx:CSlangParser.ClassbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#const_decl.
    def visitConst_decl(self, ctx:CSlangParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#full_form_const.
    def visitFull_form_const(self, ctx:CSlangParser.Full_form_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#var_decl.
    def visitVar_decl(self, ctx:CSlangParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#short_form.
    def visitShort_form(self, ctx:CSlangParser.Short_formContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#short_identifier_list.
    def visitShort_identifier_list(self, ctx:CSlangParser.Short_identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#full_form.
    def visitFull_form(self, ctx:CSlangParser.Full_formContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#identifier_list.
    def visitIdentifier_list(self, ctx:CSlangParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expression_list.
    def visitExpression_list(self, ctx:CSlangParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr0.
    def visitExpr0(self, ctx:CSlangParser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr1.
    def visitExpr1(self, ctx:CSlangParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr2.
    def visitExpr2(self, ctx:CSlangParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr3.
    def visitExpr3(self, ctx:CSlangParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr4.
    def visitExpr4(self, ctx:CSlangParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr5.
    def visitExpr5(self, ctx:CSlangParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr11.
    def visitExpr11(self, ctx:CSlangParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#array_idx.
    def visitArray_idx(self, ctx:CSlangParser.Array_idxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#index_expression.
    def visitIndex_expression(self, ctx:CSlangParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operands.
    def visitOperands(self, ctx:CSlangParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#subexpression.
    def visitSubexpression(self, ctx:CSlangParser.SubexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#compare_ops.
    def visitCompare_ops(self, ctx:CSlangParser.Compare_opsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#whole_type.
    def visitWhole_type(self, ctx:CSlangParser.Whole_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#core_type.
    def visitCore_type(self, ctx:CSlangParser.Core_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#id_type.
    def visitId_type(self, ctx:CSlangParser.Id_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#at_id.
    def visitAt_id(self, ctx:CSlangParser.At_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arr_type.
    def visitArr_type(self, ctx:CSlangParser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#class_create.
    def visitClass_create(self, ctx:CSlangParser.Class_createContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#funct_declare.
    def visitFunct_declare(self, ctx:CSlangParser.Funct_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#funct_prototype.
    def visitFunct_prototype(self, ctx:CSlangParser.Funct_prototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#params.
    def visitParams(self, ctx:CSlangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#parameter_list.
    def visitParameter_list(self, ctx:CSlangParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#parameter_declare.
    def visitParameter_declare(self, ctx:CSlangParser.Parameter_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#funct_body.
    def visitFunct_body(self, ctx:CSlangParser.Funct_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#function_call_stmt.
    def visitFunction_call_stmt(self, ctx:CSlangParser.Function_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#function_call.
    def visitFunction_call(self, ctx:CSlangParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#function_call_params.
    def visitFunction_call_params(self, ctx:CSlangParser.Function_call_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#function_call_param_list.
    def visitFunction_call_param_list(self, ctx:CSlangParser.Function_call_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#funct_return_type.
    def visitFunct_return_type(self, ctx:CSlangParser.Funct_return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continue_statement.
    def visitContinue_statement(self, ctx:CSlangParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#break_statement.
    def visitBreak_statement(self, ctx:CSlangParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_statement.
    def visitReturn_statement(self, ctx:CSlangParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_statement.
    def visitBlock_statement(self, ctx:CSlangParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stateVinhs.
    def visitStateVinhs(self, ctx:CSlangParser.StateVinhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stateVinh.
    def visitStateVinh(self, ctx:CSlangParser.StateVinhContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assignment_statement.
    def visitAssignment_statement(self, ctx:CSlangParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assignment_content.
    def visitAssignment_content(self, ctx:CSlangParser.Assignment_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#lhs.
    def visitLhs(self, ctx:CSlangParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_expressions.
    def visitAssign_expressions(self, ctx:CSlangParser.Assign_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_statement.
    def visitIf_statement(self, ctx:CSlangParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#pre_state.
    def visitPre_state(self, ctx:CSlangParser.Pre_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#bool_expression.
    def visitBool_expression(self, ctx:CSlangParser.Bool_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#true_statements.
    def visitTrue_statements(self, ctx:CSlangParser.True_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#else_expression.
    def visitElse_expression(self, ctx:CSlangParser.Else_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_statement.
    def visitFor_statement(self, ctx:CSlangParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_body.
    def visitFor_body(self, ctx:CSlangParser.For_bodyContext):
        return self.visitChildren(ctx)



del CSlangParser