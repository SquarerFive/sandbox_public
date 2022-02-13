// THIS IS A GENERATED FILE! DO NOT EDIT!


export class OtherTestObject {
    // This is another test object

    // Number of items
    count?: number;

    constructor(In_count?: number) {
        this.count = In_count;
    }

}

class VARIABLED {
    static ABC: string = "ABC";
    static XYZ: string = "XYZ";
}

class VARIABLEE {
    static LOW: number = 2;
    static HIGH: number = 4;
}

export class TestObject {
    // This is a test object

    // This property represents an integer. It is not
    // required
    variableA?: number = 24;

    // This property is a string. It is required
    variableB: string;

    // This is an object variable
    variableC?: OtherTestObject;

    // enum-like value
    variableD: string = VARIABLED.ABC;

    // enum-like value int
    variableE?: number = VARIABLEE.LOW;

    // This is an array of integers
    arrayVariable?: Array<number>;

    // This is an array of arrays of integers
    arrayOfArrays?: Array<Array<number>>;

    // This is an array of objects
    arrayOfObjects?: Array<OtherTestObject>;

    constructor(In_variableB: string, In_variableC?: OtherTestObject, In_arrayVariable?: Array<number>, In_arrayOfArrays?: Array<Array<number>>, In_arrayOfObjects?: Array<OtherTestObject>, In_variableA: number = 24, In_variableD: string = VARIABLED.ABC, In_variableE: number = VARIABLEE.LOW) {
        this.variableB = In_variableB;
        this.variableC = In_variableC;
        this.arrayVariable = In_arrayVariable;
        this.arrayOfArrays = In_arrayOfArrays;
        this.arrayOfObjects = In_arrayOfObjects;
        this.variableA = In_variableA;
        this.variableD = In_variableD;
        this.variableE = In_variableE;

        this.Validate()
    }


    Validate(): void {
        if (!(this.variableD==VARIABLED.ABC||this.variableD==VARIABLED.XYZ)) {
            console.error("Failed to validate field variableD!")
        }
        if (!(this.variableE==VARIABLEE.LOW||this.variableE==VARIABLEE.HIGH)) {
            console.error("Failed to validate field variableE!")
        }
    }
}

