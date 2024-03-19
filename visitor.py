# type: ignore
from __future__ import annotations
from abc import ABC, abstractmethod
from multimethod import multimethod
from dataclasses import dataclass


class Node(ABC):
    @abstractmethod
    def accept(self: Node, v: Visitor):
        v.visit(self)


class Visitor(ABC):
    @abstractmethod
    def visit(self: Visitor, n: Node):
        pass


@dataclass
class One(Node):
    name: str = "One"

    def accept(self: One, v: Visitor):
        return super().accept(v)


@dataclass
class Two(Node):
    name: str = "Two"

    def accept(self: Two, v: Visitor):
        return super().accept(v)


class VisitOne(Visitor):
    def visit(self: VisitOne, n: Node):
        match n:
            case One():
                print(n.name)
            case _:
                pass


class VisitMulti(ABC):
    @multimethod
    def visit(self: VisitMulti, n: One):
        pass

    @multimethod
    def visit(self: VisitMulti, n: Two):
        pass


class VisitOneMulti(VisitMulti):
    @multimethod
    def visit(self: VisitOneMulti, n: One):
        print(n.name)


def main():
    one = One()
    two = Two()
    v = VisitOne()
    one.accept(v)
    # Shouldn't print anything
    two.accept(v)
    v_multi = VisitOneMulti()
    one.accept(v_multi)
    # raises an error
    # two.accept(v_multi)


if __name__ == "__main__":
    main()
