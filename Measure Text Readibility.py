import nltk
nltk.download('punkt')

from readability import Readability

text = 'Six Sigma is a recognized standard in the manufacturing world. Jack Welch, one of the world’s most renowned leaders, most notably in his role as chairman and CEO at General Electric, defines Six Sigma as “a quality program that, when all is said and done, improves your customer’s experience, lowers your costs, and builds better leaders.” Essentially, Six Sigma is a data-driven discipline that eliminates defects in any process to improve quality and profitability. Six Sigma is a data-driven discipline that eliminates defects in any process to improve quality and profitability. Organizations that want to enhance profitability or that already use Six Sigma elsewhere in the value chain often ask, “Can Six Sigma be applied to the sales process?” The answer is, “Yes!” It starts with minimizing defects and then cutting out unnecessary steps by identifying what to measure, assessing and augmenting your team, and converting best practices to common practices. Cutting Unnecessary Steps 1. Identify the criteria to measure. A Six Sigma principle is to measure the inputs to any process and report on the outputs. In sales, the outputs are the results or orders. Identify the few vital (rather than the many trivial) key management inputs that are qualifying factors assigned to the opportunities in the pipeline  2. Assess your capabilities.The whole concept of Six Sigma in manufacturing is to reduce defects that drive costs – the cost of reworking, returns, poor quality – into the management process. Sales managers must focus on reducing defects that drive up costs, such as wasting time on unproductive sales calls, counterproductive conversations and circling back to unqualified opportunities. To limit a sales team’s exposure to these costs, establish a consistent methodology and sales process. Successful execution requires diligent preparation for engaging, purposeful interaction in order to be more productive. This process helps to weed out unqualified leads and minimize prospect variation. Remember, in Six Sigma, variation is the enemy. Successful execution requires diligent preparation for engaging, purposeful interaction in order to be more productive. By consistently and rigorously qualifying prospects, you can minimize the variations in the pipeline and focus on qualified opportunities. Time and resources wasted on no-decision opportunities are unrecoverable costs to a sales organization. 3. Leverage best practices. A quality initiative in any process will incorporate best practices. Why reinvent the wheel? Converting best practices to common practices is key to a successful sales process. Eliminating Variation The recipe for success is making sure you are generating predictable outcomes. Just as all great chefs have their own recipes to eliminate the variation in their end products, leaders in world-class sales organizations rely on a sales process to reduce the variations in qualified prospecting and, thus, maximize their revenue and margins. The recipe for success is making sure you are generating predictable outcomes. A sale team is no different than a manufacturing organization. Think of sales as the manufacturing arm of any business that “manufacturers” customers from the “raw materials” of leads and prospects. Think of sales as the manufacturing arm that “manufacturers” customers from the “raw materials” of leads and prospects. Does your customer manufacturing process deliver the results you expect? Are you managing the vital few inputs that will maximize the quality of your results? To answer with an emphatic “Yes!”, implement a Six Sigma sales process that enables you to reach short-term goals as well as your long-term strategic imperatives. A Six Sigma sales processenables you to reach short-term goals as well as your long-term strategic imperatives.'

r = Readability(text)

#Replace the below with the desired readability metric (see readability list below)
r.flesch_kincaid()

# Readability List - other readability metrics

# r.flesch_kincaid()
# r.flesch()
# r.gunning_fog()
# r.coleman_liau()
# r.dale_chall()
# r.ari()
# r.linsear_write()
# r.smog()
# r.spache()

dc = r.flesch_kincaid()

print(dc.score)
print(dc.grade_level)
