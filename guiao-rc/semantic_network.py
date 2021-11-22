

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl
    def __str__(self):
        return str(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))

    def list_associations(self):
        l=[]
        for decl in self.declarations:
            if isinstance(decl.relation,Association):
                l.append(decl.relation.name)
        return set(l)

    def list_objects(self):
        l=[]
        for decl in self.declarations:
            if isinstance(decl.relation,Member):
                l.append(decl.relation.entity1)
        return set(l)


    def list_users(self):
        l=[]
        for decl in self.declarations:
            if isinstance(decl.relation,Association):
                l.append(decl.user)
        return set(l)

    def list_types(self):
        l1=[]
        l2=[]
        for decl in self.declarations:
            if isinstance(decl.relation,(Member,Subtype)):
                l1.append(decl.relation.entity2)
            if isinstance(decl.relation,Subtype):
                l2.append(decl.relation.entity1)
        return set(l1+l2)
        
    def associations_by_user(self,user):
        l=[]
        for decl in self.declarations:
            if isinstance(decl.relation,Association) and decl.user==user:
                l.append(decl.relation.name)
        return len(set(l))
    
    def list_relations_by_user(self,user):
        l=[]
        for decl in self.declarations:
            if decl.user==user:
                l.append(decl.relation.name)
        return set(l)
        
    def list_local_associations(self,entity):
        l=[]
        for decl in self.declarations:
            if isinstance(decl.relation,Association) and decl.relation.entity1==entity:
                l.append(decl.relation.name)
        return set(l)
    
    def list_local_associations_by_user(self,entity):
        l=[]
        for decl in self.declarations:
            if isinstance(decl.relation,Association) and (decl.relation.entity1==entity or decl.relation.entity2==entity):
                l.append((decl.relation.name,decl.user))
        return set(l)

    def predecessor(self,A,B):
        predecA=False
        for decl in self.declarations:
            if isinstance(decl.relation,(Member,Subtype)) and decl.relation.entity1==A:
                predecA=True
        return predecA