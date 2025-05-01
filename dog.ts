// Base class
class Animal {
    protected name: string;
  
    constructor(name: string) {
      this.name = name;
    }
  
    makeSound(): void {
      console.log("Animal makes a sound");
    }
  
    describe(): void {
      console.log(`This is an animal named ${this.name}.`);
    }
  }
  
  // Derived class
  class Dog extends Animal {
    constructor(name: string) {
      super(name);
    }
  
    override makeSound(): void {
      console.log(`${this.name} says: Dog barks`);
    }
  }
  
  // Example usage
  const myDog = new Dog("Bruno");
  myDog.describe();        // Output: This is an animal named Bruno.
  myDog.makeSound();       // Output: Bruno says: Dog barks
  