# Introduction to RL

###### tags: `RL`

> Sergey Levine Deep RL course lecture-3 notes.

### Markov Chain 
$M = \{S,T\}$
- S - States(set of valid states that system can occupy)
- T- Transition Operator, it defines the conditional distribution over the next state given the current state. It is called operator because in discrete state spaces, it is convenient to express it as operator. We can define T as matrix of probabilities of going from one state to another in discrete spaces.
$$
p(s_{t+1}|s_{t})
$$

### Markov Decision Process 
We're gonna two things - actions and rewards to out markov chains. 
![](https://i.imgur.com/yER7xq5.png)

**In case of partially observable environment.**
![](https://i.imgur.com/2LUDWgu.png)

States give rise to observations and states + actions give rise to next state. 

### Goal of RL
Usually we want to produce a policy represented by $\pi_{\theta}(a|s)$. $\theta$ represents the weights of neural-net if we choose to work with DNNs.
![](https://i.imgur.com/Ccx57Xh.png)

Assuming a finite horizon case i.e only finite number of sequential decision steps. 

$$
p_{\theta}(s_{1},a_{1},....s_{T},a_{T}) = p(s_{1})\prod_{t=1}^{t=T}\pi_{\theta}(a_{t}|s_{t})p(s_{t+1}|s_{t},a_{t})
$$
This represents probability of a whole trajectory, it can also be written as $p_{\theta}(\tau)$.
Now we want to find weights of our network s.t
$$
\theta^{*} = arg max_{\theta} E_{\tau \sim  p_{\theta}(\tau)}(\sum_{t=0}^{t=T}r(s_{t},a_{t}))
$$



:rocket: 

### Step 2: Write something in Markdown

Let's try it out!
Apply different styling to this paragraph:
**HackMD gets everyone on the same page with Markdown.** ==Real-time collaborate on any documentation in markdown.== Capture fleeting ideas and formalize tribal knowledge.

- [x] **Bold**
- [ ] *Italic*
- [ ] Super^script^
- [ ] Sub~script~
- [ ] ~~Crossed~~
- [x] ==Highlight==

:::info
:bulb: **Hint:** You can also apply styling from the toolbar at the top :arrow_upper_left: of the editing area.

![](https://i.imgur.com/Cnle9f9.png)
:::

> Drag-n-drop image from your file system to the editor to paste it!

### Step 3: Invite your team to collaborate!

Click on the <i class="fa fa-share-alt"></i> **Sharing** menu :arrow_upper_right: and invite your team to collaborate on this note!

![permalink setting demo](https://i.imgur.com/PjUhQBB.gif)

- [ ] Register and sign-in to HackMD (to use advanced features :tada: ) 
- [ ] Set Permalink for this note
- [ ] Copy and share the link with your team

:::info
:pushpin: Want to learn more? ➜ [HackMD Tutorials](https://hackmd.io/c/tutorials) 
:::

---

## BONUS: More cool ways to HackMD!

- Table

| Features          | Tutorials               |
| ----------------- |:----------------------- |
| GitHub Sync       | [:link:][GitHub-Sync]   |
| Browser Extension | [:link:][HackMD-it]     |
| Book Mode         | [:link:][Book-mode]     |
| Slide Mode        | [:link:][Slide-mode]    | 
| Share & Publish   | [:link:][Share-Publish] |

[GitHub-Sync]: https://hackmd.io/c/tutorials/%2Fs%2Flink-with-github
[HackMD-it]: https://hackmd.io/c/tutorials/%2Fs%2Fhackmd-it
[Book-mode]: https://hackmd.io/c/tutorials/%2Fs%2Fhow-to-create-book
[Slide-mode]: https://hackmd.io/c/tutorials/%2Fs%2Fhow-to-create-slide-deck
[Share-Publish]: https://hackmd.io/c/tutorials/%2Fs%2Fhow-to-publish-note

- LaTeX for formulas

$$
x = {-b \pm \sqrt{b^2-4ac} \over 2a}
$$

- Code block with color and line numbers：
```javascript=16
var s = "JavaScript syntax highlighting";
alert(s);
```

- UML diagrams
```sequence
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
Note left of Alice: Alice responds
Alice->Bob: Where have you been?
```
- Auto-generated Table of Content
[ToC]

> Leave in-line comments! [color=#3b75c6]

- Embed YouTube Videos

{%youtube PJuNmlE74BQ %}

> Put your cursor right behind an empty bracket {} :arrow_left: and see all your choices.

- And MORE ➜ [HackMD Tutorials](https://hackmd.io/c/tutorials)
