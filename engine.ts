class Car {
    private engineNo: string;
    public brand: string;
    public model: string;
  
    constructor(engineNo: string, brand: string, model: string) {
      this.engineNo = engineNo;
      this.brand = brand;
      this.model = model;
    }
  
    
    displayInfo(): void {
      console.log("Car Details:");
      console.log(`Brand: ${this.brand}`);
      console.log(`Model: ${this.model}`);
      console.log(`Engine Number: ${this.getEngineNo()}`);
    }
  
    // Getter method for engine number (private property)
    private getEngineNo(): string {
      return this.engineNo;
    }
  }
  
  const car1 = new Car("ENG987654321", "Toyota", "Camry");
  car1.displayInfo();
  
 
  