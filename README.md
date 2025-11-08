Project Plan — PyTorch Parameter Tuning Lab
🔹 A. Project Setup

This project explores how hyperparameter tuning impacts model performance across different types of datasets.

Datasets:
Select three datasets — one tabular, one image, and one text.
(Example: Iris, MNIST, and IMDb Sentiment)

Baseline Models:

Build a simple model for each dataset using default hyperparameters.

Record accuracy, loss, and training time.

Save the trained model as a benchmark for later comparisons.

Systematic Experiments:

Vary one hyperparameter at a time while keeping others constant.

Observe how each change affects training stability and final accuracy.

Record results and include short notes explaining why performance changed.

⚙️ B. Variables / Hyperparameters to Experiment With
Category	Parameters
Learning Rate	0.001 → 0.01 → 0.1
Optimizer Type	SGD, Adam, RMSProp
Model Architecture	Vary number of layers and neurons
Activation Function	ReLU, Tanh, LeakyReLU
Regularization	Dropout rate, L2 weight decay
Training Setup	Batch size, number of epochs
Data Preprocessing	Normalization, augmentation (for images)
🔬 C. Experiment Workflow

Load and preprocess dataset → split into train, validation, and test sets.

Define a PyTorch model architecture.

Choose optimizer, loss function, and initial hyperparameters.

Train the model while tracking:

Training loss

Validation loss

Validation accuracy

Evaluate the trained model on the test set.

Visualize loss vs epochs and accuracy vs epochs.

Log results for each experiment, including:

Dataset, architecture, learning rate, optimizer, batch size, epochs, etc.

Observations like “accuracy improved because…” or “overfitting detected when…”

Repeat experiments by changing one hyperparameter at a time.

Compare and interpret the patterns across all datasets —
Do certain hyperparameters matter more for images vs tabular data?

📅 D. Milestones & Deliverables
Milestone	Objective
1️⃣ Baseline Runs	Train baseline models for all datasets
2️⃣ Learning Rate & Optimizer	Experiment with different learning rates and optimizers
3️⃣ Architecture & Regularization	Tune hidden layers, activation functions, and dropout
4️⃣ Summary & Analysis	Compare all results and document key insights

Deliverables:

Experiment notebooks (.ipynb)

CSV log of results and metrics

Plots of loss and accuracy curves

Final research-style summary and conclusions
