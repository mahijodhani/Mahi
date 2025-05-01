class Student {
    public name: string;
    private rollNo: number;
    protected course: string;
  
    constructor(name: string, rollNo: number, course: string) {
      this.name = name;
      this.rollNo = rollNo;
      this.course = course;
    }
  
    
    displayDetails(): void {
      console.log(`Name: ${this.name}`);
      console.log(`Roll No: ${this.rollNo}`);
      console.log(`Course: ${this.course}`);
    }
  }
  

  const student1 = new Student("Himesh", 101, "Computer Engineering");
  student1.displayDetails();

  