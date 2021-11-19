from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Pokemon(Base):
    __tablename__ = "pokemon"

    id      = Column(Integer, primary_key = True)
    name    = Column(String)
    number  = Column(Integer)
    atk     = Column(Integer)
    defense = Column(Integer)
    spAtk   = Column(Integer)
    spDef   = Column(Integer)
    spe     = Column(Integer)
    type1   = Column(Integer, ForeignKey("type.id"))
    type2   = Column(Integer, ForeignKey("type.id"), nullable = True)
    img     = Column(String, nullable = True)


class Move(Base):
    __tablename__ = "move"

    id          = Column(Integer, primary_key = True)
    name        = Column(String)
    power       = Column(Integer)
    precision   = Column(Integer)
    priority    = Column(Integer)
    category    = Column(Boolean)
    typeId      = Column(Integer, ForeignKey("type.id"))


class Type(Base):
    __tablename__ = "type"

    id      = Column(Integer, primary_key = True)
    name    = Column(String)
    color   = Column(String)


class Object(Base):
    __tablename__ = "object"

    id      = Column(Integer, primary_key = True)
    name    = Column(String)
    effect  = Column(String)


class Ability(Base):
    __tablename__ = "ability"

    id      = Column(Integer, primary_key = True)
    name    = Column(String)
    effect  = Column(String)


class Nature(Base):
    __tablename_ = "nature"

    id          = Column(Integer, primary_key = True)
    name        = Column(String)
    statUp      = Column(String)
    statDown    = Column(String)


class Effectiveness(Base):
    __tablename__ = "effectiveness"

    atkType = Column(Integer, ForeignKey("type.id"))
    defType = Column(Integer, ForeignKey("type.id"))
    rate    = Column(Integer)


class HasAbility(Base):
    __tablename__ = "hasAbility"

    pokeId      = Column(Integer, ForeignKey("pokemon.id"))
    abilityId   = Column(Integer, ForeignKey("ability.id"))


class LearnsMove(Base):
    __tablename__ = "learnsMove"

    pokeId  = Column(Integer, ForeignKey("pokemon.id"))
    moveId  = Column(Integer, ForeignKey("move.id"))