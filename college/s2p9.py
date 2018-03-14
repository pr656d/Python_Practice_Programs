"""
#    Given the family relationship below output all persons who fit in the input characteristic.
#    These characteristic are sibling, parent, child, grandparent and grandchild.
#    family 1 -> Ann and Marty have children Bill, Cathy and Frank. Cathy and Don have children
#               Madd and Sally. Frank and Jill have child Sarah. Bill and Alice have no children.
#    family 2 -> Debbie and Phill have children Jill and Betty. Jill and Frank have child Sarah.
#                Betty and Paul have children Marry, Jane and Bart
"""

relation = input("Enter the relationship:")
name = input("Enter the name:")
if relation == "parents" and (name == "madd" or name == "sally"):
    print("parents are cathy and don")
elif relation == "parents" and name == "sarah":
    print("parents are frank and jill")
elif relation == "parents" and (name == "frank" or name == "cathy" or name == "bill"):
    print("parents are ann and marty")
elif relation == "parents" and (name == "bart" or name == "mary" or name == "jane"):
    print("parents are betty and paul")
elif relation == "parents" and (name == "jill" or name == "betty"):
    print("parents are debby and phil")
elif relation == "child" and (name == "ann" or name == "marty"):
    print("child ren are bill , cathy and frank")
elif relation == "child" and (name == "cathy" or name == "don"):
    print("children are madd and sally")
elif relation == "child" and (name == "frank" or name == "jill"):
    print("child is sarah")
elif relation == "child" and (name == "debby" or name == "phil"):
    print("children are jill and betty")
elif relation == "child" and (name == "alice" or name == "bill"):
    print("NO child")
elif relation == "child" and (name == "paul" or name == "betty"):
    print("child ren are bart , mary and jane")
elif relation == "grandParent" and (name == "madd" or name == "sally" or name == "sarah"):
    print("grandparents are ann and marty")
elif relation == "grandParent" and (name == "sarah" or name == "bart" or name == "mary" or name == "jane"):
    print("grandparents are debby and phil")
elif relation == "grandchild" and (name == "ann" or name == "marty"):
    print("grandchild are madd , sally  and sarah")
elif relation == "grandchildren" and (name == "debby" or name == "phil"):
    print("grandchildren are sarah , bart , mary and jane")
elif relation == "sibbling" and name == "madd":
    print("sibbling is sally")
elif relation == "sibbling" and name == "sally":
    print("sibbling is madd")
elif relation == "sibbling" and name == "bill":
    print("sibbling are cathy and frank")
elif relation == "sibbling" and name == "cathy":
    print("sibbling are bill and frank")
elif relation == "sibbling" and name == "frank":
    print("sibbling are bill and cathy")
elif relation == "sibbling" and name == "bart":
    print("sibbling are mary and jane")
elif relation == "sibbling" and name == "mary":
    print("sibbling are jane and bart")
elif relation == "sibbling" and name == "jane":
    print("sibbling are mary and bart")
elif relation == "sibbling" and name == "jill":
    print("sibbling is betty")
elif relation == "sibbling" and name == "betty":
    print("sibbling is jill")
elif relation == "sibbling" and name == "sarah":
    print("NO sibblings")
