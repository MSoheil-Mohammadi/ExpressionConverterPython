from Converters.InfixConverter import InfixConverter
from Converters.PostfixConverter import PostfixConverter
from Converters.PrefixConverter import PrefixConverter
from Tree.Draw import postfix_draw, prefix_draw
from Tree.Print import print_tree

print(InfixConverter().convert('(a+b)-c'))
print(PostfixConverter().convert('ab+c-'))
print(PrefixConverter().convert('-+123'))

print_tree(postfix_draw("23^4^"))
print_tree(prefix_draw("+^+343+56"))

print_tree(postfix_draw(InfixConverter().toPostfix("(2^3)^4")))
print_tree(prefix_draw(InfixConverter().toPrefix("(2^3)^4")))