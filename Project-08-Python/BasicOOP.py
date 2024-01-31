class DataAnalyst:
  def __init__(self, name, expertise, experience):
      self.name = name
      self.expertise = expertise
      self.experience = experience

  def display_information(self):
      """Display basic information about the data analyst."""
      print(f"Name: {self.name}")
      print(f"Expertise: {self.expertise}")
      print(f"Experience: {self.experience} years")

  def analyze_data(self, dataset):
      """Analyze the given dataset."""
      print(f"{self.name} is analyzing the data with expertise in {self.expertise}")

  def suggest_improvements(self):
      """Suggest improvements based on data analysis."""
      print(f"{self.name} suggests improvements based on the data analysis.")
  def collaborate(self, colleague):
      """Collaborate with another data analyst."""
      print(f"{self.name} is collaborating with {colleague}'s expertise.")


# Example usage of the DataAnalyst class
analyst1 = DataAnalyst(name="Golf", expertise="Machine Learning", experience=3)
analyst1.display_information()
analyst1.analyze_data(dataset="Sales Data")
analyst1.suggest_improvements()
analyst1.collaborate(colleague = Mike )

analyst2 = DataAnalyst(name="Golf", expertise="Data Visualization", experience=5)
analyst2.display_information()
analyst2.analyze_data(dataset="Customer Satisfaction Survey")
analyst2.suggest_improvements()
analyst2.collaborate(colleague = Golf)
