// THIS IS A GENERATED FILE! DO NOT EDIT!


export class OtherTestObject {
    // [[GENERATED_OBJECT]] This is another test object


    // Number of items
    count?: number;

    constructor(In_count?: number) {
        this.count = In_count;
    }

}

export class VARIABLED {
    static ABC: string = "ABC";
    static XYZ: string = "XYZ";
}

export class VARIABLEE {
    static LOW: number = 2;
    static HIGH: number = 4;
}

export class TestObject {
    // [[GENERATED_OBJECT]] This is a test object


    // This property represents an integer. It is not
    // required
    variableA?: number = 24;

    // This property is a string. It is required
    variableB: string;

    // This is an object variable
    variableC?: OtherTestObject;

    // enum-like value
    variableD: string;

    // enum-like value int
    variableE?: number;

    constructor(In_variableB: string, In_variableD: string, In_variableC?: OtherTestObject, In_variableE?: number, In_variableA: number = 24) {
        this.variableB = In_variableB;
        this.variableD = In_variableD;
        this.variableC = In_variableC;
        this.variableE = In_variableE;
        this.variableA = In_variableA;
    }

}

