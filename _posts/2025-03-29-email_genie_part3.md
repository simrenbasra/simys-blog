---
title: "Email Genie: Word Embeddings 🧩"
date: 2025-03-29
---

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/word_embedding_cover_photo.jpg" alt="cover photo" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

In the previous post, I introduced the concept of vectorising text to gain insights into the Enron dataset using TF-IDF. This allowed me to explore the most important terms and themes in the data, providing a deeper understanding of the factors contributing to the downfall of Enron. While TF-IDF revealed a lot about the data, its insights were somewhat limited. The method primarily focuses on word frequency and importance, without capturing the broader context or relationships between words.

Since the goal of this project is to build a classifier, leveraging semantic relationships between words can help models perform better. This is where word embeddings come in!

In this post, I will explain word embeddings and explore a common embedding model:  Word2Vec!

<br>

----

<br>

## Word Embeddings

Word embeddings are another way to turn words into vectors, allowing Machine Learning models to understand them. Unlike TF-IDF, which focuses on word frequency and importance, word embeddings learn the context and relationships between words from large text datasets.

Let’s take a look at a simple example:

**Document A:** *“Today, I went to the bank to deposit some money”*

**Document B:** *“Today, I sat by the bank of a river and had lunch”*

TF-IDF treats the word *“bank”* the same in both documents. It fails to recognise the two different meanings and only considers the word without any context.

However, word embeddings look at the surrounding words to understand a word’s meaning:

In document A bank is related to money.

In document B bank is related to a river.

And so, in the vector space bank will have two vectors: one will be close to vectors for money and finance, the other closer to vectors for rivers and nature. 

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/bank_vectors.png" alt="bank vectors" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

Another interesting thing you can do with word embeddings is word arithmetic. Word arithmetic describes process of performing operations with words to find relationships.

**Example:**

`Teacher – School + Hospital = Doctor`

A teacher works at a school, if we remove School and replace it with Hospital, the embeddings return Doctor. Just as a teacher works in a school, a doctor works in a hospital.

**Relating back to Document A and B**

`Bank – river + deposit = money`

Here, we remove the river-related meaning of "bank" and add "deposit," shifting the meaning toward finance, leading to money.

<br>

----

<br>

## How are word embeddings created?

Word embeddings are created by training a neural network to predict words based on context. Over time, the network updates its weights, and these weights become the word embeddings. The main purpose of word embeddings is to represent words as vectors where similar words have similar vectors. This allows the model to interpret semantics between words by assessing how close these vectors are.

Take the example below, let’s break it down step by step.

**Document A:** *“The cat sat on the sofa”*

**Document B:** *“The cat sat on the chair”*

**Corpus:** [ *"cat", "sat", "on", "the", "chair", "sofa"*]

To help understand this process, I have created a diagram:

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/updated_w2v_diagram.png" alt="word embedding diagram" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

#### **Step 1:** 

Each word in the vocabulary is represented as a one-hot encoded vector. For this example we are focusing on "cat" and its one-hot vector is:`[1,0,0,0,0,0,0]`.

Before training begins, we prepare the training data by creating word pairs of target and context words based on the window size.

In our example where the window size is 1, the target word will have two context words: one to the left and one to the right. So, the word pairs for this example are:

- (cat, the)

- (cat, sat)

The model starts with no understanding of words. These word pairs help the model learn patterns of which words appear together.

For example, the pair *(cat, sat)* tells the model that *"cat"* and *"sat"* often appear close to each other. Over time, the model pulls the vector for *"cat"* closer to relevant context words like *"sat"* and pushes it away from unrelated words. As training continues, the model becomes better at recognising these patterns and the embeddings become more meaningful.

#### **Step 2:** 
Like any other neural network, weights are randomly initialised.

-	Weights connecting the input layer to the hidden layer form the word embedding for “cat”. These weights control how much each input word shapes the word embedding for the target word. 

-	The number of nodes in the hidden layer determine the size of the word embeddings, here there are 7 nodes and so the embeddings have a length of 7.

#### **Step 3:**  

Weights between the hidden layer to the output layer are not part of the word embedding, they are used to predict which words follow the word *"cat"*.

#### **Step 4:**

At first, the model makes random predictions since the weights are not yet trained. As you can see, the probabilities do not make much sense.

#### **Step 5:**

After the first pass, the model calculates error by comparing its predictions to the true context words. The actual context words are set using a window size, a window size of 1 the context words are: [*"the", "sat"*]. I will revisit this later in the post! 

The calculated loss is then backpropagated, the network updates its weights to minimise the loss to improve its predictions. 

#### **Step 6:**

After a few epochs of training, the word embeddings starts to reflect more meaningful relationships between the words. The network uses these embeddings to predict which words are most likely to follow the word “cat” and as a result, the predictions become more reasonable.

Once training is complete, the word embedding for cat looks something like this:

`[0.0, 0.3, 0.2, 0.3, 0.1, 0.5]`

<br>

----

<br>

## Word 2 Vec 

For my project, I used the Word2Vec model, as it is a well-known model for creating embeddings and so thought it a great starting point for me!

#### **What is Word2Vec?**

Word2Vec was created by Google to learn word embeddings from large datasets. It has two main approaches:

**1. Continuous Bag of Words (CBOW)**

Predicts the middle word given the surrounding words.

**Example:** The cat sat on the chair

**Input:** [“the” , “cat”, “on”, “chair”] 

**Output:** [“sat”]

**2. Skip-Gram:**

Predicts the surrounding word given the middle word.

**Input:** [“sat”] 

**Output:** [“the”,  “cat”, “on”, “chair” ]

Both methods use a similar network to the one described above with the main difference in what we’re predicting. 

In my project I chose to use Skip-Gram as with email data there are more specific, rare words like domain specific terms. Since Skip-Gram predicts context from a single word, I thought it be better at capturing relationships in the email data. 

#### **Negative Sampling**

When dealing with large datasets, updating the weights for every word can be quite time consuming. Word2Vec speeds up the training process by using negative sampling.
Instead of updating all words in the dataset, negative sampling focuses on a smaller set of relevant words while ignoring irrelevant ones. 

For this explanation assume the corpus has expanded to include words not in document A or B. So, we now have:

**Target word**: "cat"

**Document A**: "The cat sat on the chair"

**Document B**: "The cat sat on the sofa"

**Document C**: “The sky is blue”

**Document D**: “Computers are fast”

Word pairs created during training only come from documents where the target word appears (A and B). These are called positive word pairs and represent relevant context words for “cat”.

Now, for the irrelevant words. Word2Vec randomly selects words from the entire corpus from documents that don't have the target word. These are negative word pairs:

(cat, sky), (cat, computer)

The model uses these pairs to learn what is *not* related to the target word, reducing the probability of predicting these words. The number of negative pairs is controlled by a `negative_sampling_rate` parameter. The parameter determines how many negative samples are selected for each positive pair, so if `negative_sampling_rate = 2` that means for every positive word pair, the model will randomly select 2 negative pairs.


#### **How to Implement Word2Vec**

**Step 1: Preparing Text**

Like implementing TF-IDF, the first step is to prepare the dataset for processing. I began by combining the subject and body of each email. I did this as I thought it would help the model to understand more context of an email. Usually, the subject provides a summary of an email, which can help models understand key themes in an email.

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/all_text.png" alt=" preprocess_1" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

Like I did in implementing TF-IDF, I also used NER to remove the employee names, dates, and organisations from emails to reduce noise.

**Step 2: Tokenising Text**

Before training the Word2Vec model, emails need to be tokenised. Unlike TF-IDF, where I tokenise individual words, here I tokenise entire emails since Word2Vec requires context to learn embeddings. 

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/tokeniser.png" alt="tokeniser" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>


<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/tokenising_all_emails.png" alt="tokenising each email" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

**Note:** I decided not to use stop words here, this is as small words such as _“with”_, _“and”_, _“for”_ could be quite important for the model to understand context. 

**Step 3: Instantiate the model and run!**

With each email tokenised, I implemented the Word2Vec model using the `genism` library.

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/training_w2v.png" alt="training word2vec" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

Let’s look at some of the parameters I set:

-	`sentences = tokened emails`
    
    Defines the input data into the model, for my project this was the tokenised emails.

-	`vector_size = 300` 

    Defines the size of the embeddings, in this case the network would have 300 nodes.

-	`window = 10` 

    Defines the number of words before/after the target word the model should consider when learning. 

-	`min_count = 15`
    
    Words which appear less than 15 times are ignored, I set this to help reduce noise returned.

-	`workers = 4`
    
    Number of CPU cores used in parallel processing to increase speed in training.

-	`sg = 1`

    Sets method to use: Skip gram = 1, CBOW = 0

-	`seed = 22`
    
    Setting the random seed to ensure my results are reproducible.

-	`epochs = 25`
    
    Number of times the model trains on the dataset. I chose 25 epochs as I wanted to give the model enough time to learn meaningful patterns without running the risk of overfitting. 

<br>

----

<br>

## Evaluating the Embeddings

To assess the quality of the embeddings, I wanted to see how well they captured semantic relationships between words and visualise the embeddings to see if we can start to see any groupings.

First, I needed a list of words that I could use to evaluate the embeddings. I thought it best to use insights from TF-IDF since it highlights the most meaningful words in the dataset:

**Topic #1: Finance -** risk, market, cash

**Topic #2: Operations-** operational, shipping, security

**Topic #3: Legal-** privileged, evidence, contract

#### **1. Semantic Similarity Between Embeddings**

I used the most_similar function, which uses cosine similarity to find words that are contextually similar to a given word. I wrote a function to take a word as an input and output the 5 most similar words according to the model:

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/most_similar.png" alt="most similar words function" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

#### **Overview of Results:**

**Positive Results**

For some words, the embeddings performed well, for instance: 

- "Risk" returned related terms like *"management"*, *"operational"*, and *"operation"*.

- "Market" returned *"price"*, *"energy"*, and *"power"* demonstrating its relevance to the energy trade.

- "Privileged" showed terms like *"confidential"* and *"attorney-client"* which fit well in legal context.

**Issues:**

In other cases, the results were less meaningful and contained some irrelevant terms: 

- "Security" returned terms like *"brokerdealer"* and *"screener"* which seem more relevant to the finance industry than security itself.

- "Evidence" produced words such as *"create"* and *"acceptance"* which don't really git into legal context.

Overall, these results aren't all terrible, but the embeddings could be better. Some unusual terms, like *"gidlct"* and *"reftws"* likely due to some remaining noise in the data.

Another way to assess semantic similarity is through word arithmetic. Here are some formulas I tested and the results:

**Market + Security - Risk = ["rtm", "national", "economy", "issued", "economy"]**

The results here are not ideal. Terms like *"rtm"*, *"national"*, *"economy"*, and *"issued"* seem to be more related to trading than *"market"* or *"security”*. Some of these terms like "rtm" might be noise or acronym-like terms, which don't seem to fit well in the context. 

Acronyms is something I didn't think about when cleaning data and may have to go back to the data cleaning to address this.

**Shipping + Operational - Security = ["handling", "risk", "proliferation", "underwriting", "lyon"]**

Some results like *"handling"* and *"proliferation"* make sense and are clearly related to operations. However, *"lyon"* which seems like a place or name, doesn't belong here. *"risk"* is also strange, suggesting the embeddings may be mixing up operational and financial contexts.

**Contract + Privileged - Evidence = ["confidential", "contain", "estoppel", "proprietary", "attorneyclient"]**

These results seem quite strong and meaningful. Words like *"confidential"*, *"attorneyclient"*, and *“proprietary"* align well with legal contexts.

**Cash + Market - Risk → ["price", "rtm", "flow", "realtime", "regular"]**

Not bad results, words like *"price"*, *"flow"*, and *"realtime"* are closely related to trading and finance. 

#### **2. Visualise the Embeddings**

To visualise word relationships, I reduced the dimensionality of the word vectors using t-SNE and plotted them. This helped determine whether semantically similar words were grouped close together in the vector space.


<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/tsne_init.png" alt="tsne 1" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>


<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/tsne_get_embeddings.png" alt="tsne 2" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>


<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/tsne_fit_transform.png" alt="tsne 3" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>


#### **Overview of Results**

Results from t-SNE visualisation show there is some slight groupings of embeddings.

<div style="text-align: center;">
  <img src="{{ site.baseurl }}/assets/email-genie/phase_2/visualising_embeddings.png" alt="visualising embeddings" style="max-width: 100%; height: auto; margin: 20px 0;">
</div>

**Financial** terms such as *"stock"*, *"revenue"*, *"investment"*, *"equity"*, and *"cash"* are close to each other, indicating that Word2Vec has captured some semantic relationships between financial terms.

**Operational** terms like *"logistics"*, *"efficiency"*, and *"warehouse"* also appear relatively close, suggesting that the model recognises their similarity in meaning.

**Legal** terms including *"contract"*, *"litigation"*, *"jurisdiction"*, *"liability"*, *"binding"*, and *"confidentiality"* show some grouping suggesting the model understands these words are related to each other.

However, the groupings are not well-defined, with some overlapping areas and some terms appearing far from their expected grouping such as *"risk"* and *"market"*. This suggests that while Word2Vec captures general relationships, it still is missing some context and highlights the issue in struggling with words that have multiple meanings.

<br>

----

<br>

## Summary 

The results showed that Word2Vec successfully identified relationships in financial, operational, and legal contexts, though some noise and inaccurate results highlighted areas for improvement. Next, my plan is to experiment with transformers to see if their embeddings are better.
