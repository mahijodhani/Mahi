
interface PersonInfo {
    name: string;
    age: number;
  }
  
  
  class Person implements PersonInfo {
    name: string;
    age: number;
  
    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }
  
    
    displayInfo(): void {
      console.log(`Name: ${this.name}`);
      console.log(`Age: ${this.age}`);
    }
  }
  
  
  const person1 = new Person("Mahi", 21);
  person1.displayInfo();
  