import json
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str)
    args = parser.parse_args()

    print(f"Converting examples from {args.input_file} to {args.output_file}...")

    with open(args.input_file, 'r') as inpf, open(args.output_file, 'w') as outf:
        examples = json.load(inpf)
        print(f"Found {len(examples)} examples")

        for i, example in enumerate(examples):
            sentence = example['words']
            ner = []
            relation = []
            event = []

            #Get NER information
            for example_entity in example['golden-entity-mentions']:
                entity_start = example_entity['start']
                entity_end = example_entity['end'] - 1
                entity_type = example_entity['entity-type']

                ner.append([entity_start, entity_end, entity_type])

            #Get event trigger and arguments
            for example_event in example['golden-event-mentions']:
                event_type = example_event['event-type']
                trigger = example_event['trigger']
                arguments = example_event['arguments']

                if trigger['end'] - trigger['start'] != 1:
                    print(f"WARNING: Trigger \"{trigger['text']}\" is longer than one word! Only first word will be kept.")

                converted_event = [[trigger['start'], event_type]]

                for argument in arguments:
                    converted_event.append([argument['start'], argument['end'], argument['role']])

                event.append(converted_event)

            #Create converted example
            converted_example = {
                'sentence' : sentence,
                's_start' : 0,
                'ner' : ner,
                'relation' : relation,
                'event' : event
            }
            #Write to output file
            json.dump(converted_example, outf)
            outf.write("\n")
