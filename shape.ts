
interface Shape {
    calculateArea(): number;
  }
  
  
  class Rectangle implements Shape {
    private length: number;
    private width: number;
  
    constructor(length: number, width: number) {
      this.length = length;
      this.width = width;
    }
  
    
    calculateArea(): number {
      return this.length * this.width;
    }
  
    display(): void {
      console.log(`Length: ${this.length}`);
      console.log(`Width: ${this.width}`);
      console.log(`Area: ${this.calculateArea()}`);
    }
  }
  
  
  const rect = new Rectangle(10, 5);
  rect.display();
  