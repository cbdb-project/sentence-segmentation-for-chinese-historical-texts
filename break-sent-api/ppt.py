n_epochs = 50  # number of epochs over the training set
freq_eval = len(train_data) / 10  # evaluate on dev every freq_eval steps
print 'freq_eval is ' + str(freq_eval)
print_count = 10000
best_dev = -np.inf
best_test = -np.inf
count = 0
# epoch = 0
time1 = time.time()
for epoch in xrange(n_epochs):
    # while True:
    epoch_costs = []
    print "Starting epoch %i..." % epoch
    for i, index in enumerate(np.random.permutation(len(train_data))):
        count += 1
        input = create_input(train_data[index], parameters, True, singletons)
        new_cost = f_train(*input)
        epoch_costs.append(new_cost)
        if i % print_count == 0 and i > 0 == 0:
            # print "%i, cost average: %f" % (i, np.mean(epoch_costs[-print_count:]))
            print "count %i" % (i)
            if count % freq_eval == 0:
                print 'evaluating!'
                dev_score = evaluate(parameters, f_eval, dev_sentences,
                                     dev_data, id_to_tag, dico_tags)
                test_score = evaluate(parameters, f_eval, test_sentences,
                                      test_data, id_to_tag, dico_tags)
                dev_score = evaluate_coustom()
                test_score = evaluate_coustom()
                print "Score on dev: %.5f" % dev_score
                print "Score on test: %.5f" % test_score
                if dev_score > best_dev:
                    best_dev = dev_score
                    print "New best score on dev."
                    print "Saving model to disk..."
                    model.save()
                if test_score > best_test:
                    best_test = test_score
                    print "New best score on test."
                    # print "Epoch %i done. Average cost: %f" % (epoch, np.mean(epoch_costs))
    print "Epoch %i done." % (epoch)