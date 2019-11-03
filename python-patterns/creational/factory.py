# coding=utf-8
from abc import ABC, abstractmethod


class Sharpe(ABC):

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Sharpe):

    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Sharpe):

    def draw(self):
        print("Inside Square::draw() method.")


class Circle(Sharpe):

    def draw(self):
        print("Inside Circle::draw() method.")


class ShapeFactory:

    def getShape(self, shapeType=None):
        if not shapeType or not isinstance(shapeType, str):
            return None

        if shapeType.upper() == 'CIRCLE':
            return Circle()
        elif shapeType.upper() == 'RECTANGLE':
            return Rectangle()
        elif shapeType.upper() == 'SQUARE':
            return Square()

        return None


if __name__ == '__main__':
    shape_factory = ShapeFactory()

    shape1 = shape_factory.getShape("CIRCLE")
    shape1.draw()

    shape2 = shape_factory.getShape("RECTANGLE")
    shape2.draw()

    shape3 = shape_factory.getShape("SQUARE")
    shape3.draw()
