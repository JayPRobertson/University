/*
* Student.java
* A Student class
*/


public class Student {

	private String sID;
	private int grade;

	public Student() {
		sID = "";
		grade = -1;
	}

	public Student(String sID, int grade) {
		this.sID = sID;
		this.grade = grade;
	}
	
	public String getSID() {
		return sID; 
	}
	
	public int getGrade() {
		return grade;
	}

	public void setGrade(int newGrade) {
		grade = newGrade;
	}

	public void setSID(String newSID){
		sID = newSID;
	}

	public String toString(){
		return "Student " + sID + " with grade of " + grade + "%";
	}

}

